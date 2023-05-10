from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import status
from rest_framework.views import APIView, Response
from drf_yasg.utils import swagger_auto_schema

from invites.models import Invite
from invites.serializers import InviteCreateSerializer, InviteSerializer
from user.models import Profile


class InviteDetail(generics.RetrieveAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    lookup_field = "id"


class InviteFromUserAPIView(APIView):
    def get(self, request, profile_id, *args, **kwargs):
        profile = Profile.objects.filter(id=profile_id).first()
        if profile:
            invites_from = profile.invites_from.all()
            serializer = InviteSerializer(invites_from, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No such profile"}, status=status.HTTP_404_NOT_FOUND)


class InviteToUserAPIView(APIView):
    def get(self, request, profile_id, *args, **kwargs):
        profile = Profile.objects.filter(id=profile_id).first()
        if profile:
            invites_to = profile.invites_to.all()
            serializer = InviteSerializer(invites_to, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No such profile"}, status=status.HTTP_404_NOT_FOUND)


class InviteUserAPIView(APIView):
    @swagger_auto_schema(
            request_body=InviteCreateSerializer
            )
    def post(self, request, *args, **kwargs):
        serializer = InviteCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        from_profile_id = serializer.validated_data["from_profile"]
        to_profile_id = serializer.validated_data["to_profile"]
        from_profile = Profile.objects.filter(id=from_profile_id).first()
        to_profile = Profile.objects.filter(id=to_profile_id).first()
        if to_profile and from_profile:
            already_invited = to_profile.invites_from.filter(to_profile=from_profile_id).first()
            if already_invited and not already_invited.rejected:
                to_profile.friends.add(from_profile)
                from_profile.friends.add(to_profile)
            Invite.objects.create(from_profile=from_profile, to_profile=to_profile)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "No such profile"}, status=status.HTTP_404_NOT_FOUND)
