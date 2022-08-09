from django.http import Http404
from django.http.response import JsonResponse
from .serializers import VideoSerializer
from .models import *
from rest_framework import status, filters
from .permissions import IstheUser, IsInstractor
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication


class GetVideo(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsInstractor, IstheUser]
    authentication_classes = [TokenAuthentication, ]


class UploadVideo(CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    # permission_classes = [IsInstractor, IstheUser]
    authentication_classes = [TokenAuthentication, ]
# class GetCourseVideos(ListAPIView):
#     serializer_class = VideoSerializer
#     permission_classes = [IsInstractor, IstheUser]
#     authentication_classes = [TokenAuthentication, ]
