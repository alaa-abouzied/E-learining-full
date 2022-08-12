from rest_framework import serializers
from course.models import Category, Course
# from category.serializers import Categoryerializer
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        

# class Categoryerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'        