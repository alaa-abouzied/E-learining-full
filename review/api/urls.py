from django.urls import path
from review.api.views import ReviewAPIListView, SingleReviewDetailView


urlpatterns = [
    path("index", ReviewAPIListView.as_view()),
    path("<int:id>", SingleReviewDetailView.as_view()),
]