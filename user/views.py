from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView, Response, status

from user.models import Profile

from .serializers import ProfileSerializer, UserSerializer


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


class FriendListAPIView(APIView):
    def get(self, request, profile_id, *args, **kwargs):
        profile = Profile.objects.filter(id=profile_id).first()
        if profile:
            friends = profile.frieds.all()
            serializer = ProfileSerializer(friends, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No such profile"}, status=status.HTTP_404_NOT_FOUND)
