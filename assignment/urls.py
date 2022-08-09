from django.urls import path
from . import views

urlpatterns = [
    path("",views.Assign_List),
    path("assignments/",views.Assignments_List.as_view()),
    path("assignment/<int:id>/",views.Assignment_List),
    path("assignmentm/",views.Uploade_assignment.as_view()),

]