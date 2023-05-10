from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['id', "user"]


class ProfileCreateSerializer(serializers.Serializer):
    username = serializers.CharField()


class FriendsSerializer(serializers.Serializer):
    profile_id = serializers.IntegerField()
    friend_id = serializers.IntegerField()

