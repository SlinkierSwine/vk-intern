from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView, Response, status

from user.models import Profile

from .serializers import FriendsSerializer, ProfileCreateSerializer, ProfileSerializer, UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "id"


class ProfileCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProfileCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        user = User.objects.create(username=username, password='')
        Profile.objects.create(user=user)
        return Response(status=status.HTTP_200_OK)


class FriendListAPIView(APIView):
    def get(self, request, profile_id, *args, **kwargs):
        profile = Profile.objects.filter(id=profile_id).first()
        if profile:
            friends = profile.frieds.all()
            serializer = ProfileSerializer(friends, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "No such profile"}, status=status.HTTP_404_NOT_FOUND)


class FriendStatusAPIView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = FriendsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile_id = serializer.validated_data["profile_id"]
        friend_id = serializer.validated_data["friend_id"]
        
        profile = Profile.objects.filter(id=profile_id).first()
        if profile:
            if profile.friends.filter(id=friend_id):
                return Response({"data": "You are friends"})
            if profile.invites_from.filter(to_profile=friend_id):
                return Response({"data": "You have an outgoing invite"})
            if profile.invites_to.filter(from_profile=friend_id):
                return Response({"data": "You have an incoming invite"})
            else:
                return Response({"data": "You are not friends"})
        return Response({"error": "No such profile"}, status=status.HTTP_404_NOT_FOUND)


class DeleteFriendAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        serializer = FriendsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile_id = serializer.validated_data["profile_id"]
        friend_id = serializer.validated_data["friend_id"]

        profile = Profile.objects.filter(id=profile_id).first()
        if profile:
            friend = profile.friends.filter(id=friend_id).first()
            if friend:
                profile.friends.remove(friend)
                return Response(status=status.HTTP_200_OK)
            return Response({"error": "No such friend"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "No such profile"}, status=status.HTTP_404_NOT_FOUND)
