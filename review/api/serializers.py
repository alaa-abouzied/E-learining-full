from rest_framework import serializers
from review.models import Course, Review


class CourseSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class ReviewSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"