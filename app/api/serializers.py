from rest_framework import serializers
# from django.contrib.auth.models import User, Group
from ..models import Event, Account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'created_at', 'name', 'venue', 'date', 'description', 'poster_image']