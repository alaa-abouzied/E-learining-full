from django.http import Http404
from django.http.response import JsonResponse
from .serializers import CourseSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import generics,mixins,viewsets
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IstheUser
# Create your views here.

def no_rest_no_model(request):
    courses = [
        {
            "id": 1,
            "Name": "Admin1",
            "description": "this course is for linux-redhat"
        },
        {
            "id": 2,
            "Name": "Django",
            "description": "this course is for web development using python"
        },
             ]
    return JsonResponse (courses,safe=False)
#################################################################################

def no_rest_from_model(request):
    data = Course.objects.all()
    response = {
        'courses': list(data.values('course_name', 'course_description'))
    }
    return JsonResponse(response)
#################################################################################


@api_view(['GET', 'POST'])
def FBV_List(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_404_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # , status=status.HTTP_200_ACCEPTED )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#################################################################################

class CBV_List(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )


class CBV_pk(APIView):
    def get_object(self, pk):
        try:
            return Course.object.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.dalete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#################################################################################

class mixins_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)

#################################################################################

class generics_list(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class= CourseSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated] 
    
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class= CourseSerializer
    authentication_classes = [TokenAuthentication]
#################################################################################

class viewsets_guest(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class= CourseSerializer
    authentication_classes = [TokenAuthentication]
    
#################################################################################    

@api_view(['GET'])
def find_course(request):
    courses = Course.objects.filter(
        course_name=request.data['course_name'],
        course_instructor=request.data['course_instructor'],
    )
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


class Course_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IstheUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer