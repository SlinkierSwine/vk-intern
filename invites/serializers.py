from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Invite


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['id', 'from_profile', 'to_profile']


class InviteCreateSerializer(serializers.Serializer):
    from_profile = serializers.IntegerField()
    to_profile = serializers.IntegerField()
    
