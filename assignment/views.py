from django.shortcuts import render
from .models import Assignment
from rest_framework.decorators import api_view
from .serializers import AssignmentSerializer
from rest_framework import status, filters
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
# Create your views here.
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.viewsets import ReadOnlyModelViewSet


# class AssignmentViewSet(ReadOnlyModelViewSet):
#     queryset = Assignment.objects.all()
#     serializer_class = AssignmentSerializer
    # permission_classes = [IsAuthenticated]

@api_view(['GET', 'POST'])
def Assign_List(request):
    if request.method == 'GET':
        assigment = Assignment.objects.all()
        serializer = AssignmentSerializer(assigment, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Assignment_List(request, id):
    try:
        assigment = Assignment.objects.get(id=id)
    except Assignment.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AssignmentSerializer(assigment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AssignmentSerializer(assigment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        assigment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## -------------------------- class based views ------------------------------------------
## -------------------------- list and create get and post --------------------

class Assignments_List(APIView):
    def get(self,request):
        assigment = Assignment.objects.all()
        serializer = AssignmentSerializer(assigment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        return Response(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Uploade_assignment(CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    












