from ast import Delete
from review.models import Course, Review
from review.api.serializers import CourseSerilizer, ReviewSerlizer
from rest_framework import generics

# -------------------create--view------------------------
class ReviewAPIListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerlizer

# -------------------update single review--delete review------------------------
# Retrieve---Show
# Destroy---Delete
# Update---Update
class SingleReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerlizer
    queryset = Review.objects.all()
    lookup_url_kwarg = 'id'

