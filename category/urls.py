from django.urls import path, include
from category import views
urlpatterns = [
    path('list/', views.Category_List),
    path('<int:pk>/', views.Category_pk),
]
