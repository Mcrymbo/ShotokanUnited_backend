from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import NewsSerializers, CommentSerializer, CategorySerializer
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from accounts.models import storage
from django.db import transaction
from .models import News, Like, Comment, Category
from datetime import timedelta
from rest_framework.exceptions import NotFound
from django.utils.timezone import now
from rest_framework.decorators import api_view

def upload_cover_image(cover_image):
    with cover_image.open() as img:
        storage.child(f"news_cover_images/{cover_image.name}").put(img)
        url = storage.child(f"news_cover_images/{cover_image.name}").get_url(None)
        return url

class NewsViewSets(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by category if provided
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(categories__slug=category)
            
        # Filter by search query if provided
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
            
        return queryset.order_by('-date')

    def perform_create(self, serializer):
        news_instance = serializer.save(author=self.request.user)
        if 'cover_image' in self.request.FILES:
            cover_image_url = upload_cover_image(self.request.FILES['cover_image'])
            news_instance.cover_image_url = cover_image_url
            news_instance.save()
    
    def perform_update(self, serializer):
        news_instance = serializer.save()
        if 'cover_image' in self.request.FILES:
            cover_image_url = upload_cover_image(self.request.FILES['cover_image'])
            news_instance.cover_image_url = cover_image_url
            news_instance.save()
    
    def update_trending_news(self):
        views_threshold = 10
        likes_threshold = 10
        recency_days = 7

        trending_news = News.objects.filter(
            views__gte=views_threshold,
            likes_count__gte=likes_threshold,
            date__gte=now() - timedelta(days=recency_days)
        )

        News.objects.filter(is_trending=True).update(is_trending=False)
        trending_news.update(is_trending=True)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.views += 1
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            return Response({"Error": "news not found"}, status=404)

    @action(detail=False, methods=['get'])
    def categories(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def increment_views(self, request, pk=None):
        try:
            news = News.objects.get(pk=pk)
            news.views += 1
            news.save()
            return Response({"message": "added a view", "views": news.views}, status=status.HTTP_202_ACCEPTED)
        except News.DoesNotExist:
            return Response({"Error": "news item not found"}, status=status.HTTP_404_NOT_FOUND)

class LikeNewsView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise NotFound("News Item not found")

        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key

        with transaction.atomic():
            if request.user.is_authenticated:
                like, created = Like.objects.get_or_create(user=request.user, news=news)
            else:
                like, created = Like.objects.get_or_create(session_id=session_id, news=news)

            if created:
                news.likes_count += 1
                news.save(update_fields=['likes_count'])
                return Response({"message": "Liked the news", "likes_count": news.likes_count}, status=201)
            else:
                like.delete()
                news.likes_count -= 1
                news.save(update_fields=['likes_count'])
                return Response({"message": "Unliked the news", "likes_count": news.likes_count}, status=200)

class CommentsNewsView(APIView):
    def post(self, request, pk):
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response({"Error": "News does not exists"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, news=news)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)