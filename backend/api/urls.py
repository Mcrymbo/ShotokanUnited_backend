from rest_framework.routers import DefaultRouter
# from app.api.urls import user_router, group_router, event_router
from app.api.urls import event_router, message_router
from accounts.urls import profile_router, user_router
from blog.urls import blog_router, category_router
from news.urls import news_router
from news.views import LikeNewsView, CommentsNewsView
from django.urls import path, include
from clubs.views import GenerateRegistrationLinkAPIView, RegisterAPIView
from app.views import chat_with_deepseek

router = DefaultRouter()
router.registry.extend(event_router.registry)
router.registry.extend(profile_router.registry)
router.registry.extend(message_router.registry)
router.registry.extend(user_router.registry)
router.registry.extend(news_router.registry)
router.registry.extend(blog_router.registry)
router.registry.extend(category_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('news/<uuid:pk>/like/', LikeNewsView.as_view(), name='like'),
    path('news/<uuid:pk>/comment/', CommentsNewsView.as_view(), name='comment'),
    path('generate-token/', GenerateRegistrationLinkAPIView.as_view(), name='generate-token'),
    path('register/<uuid:token>/', RegisterAPIView.as_view(), name='register'),
    path('chat/', chat_with_deepseek, name='chat_with_deepseek'),
]
