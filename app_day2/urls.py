from django.urls import path

from app_day2 import views

urlpatterns = [
    path("students/", views.StudentsAPIVIew.as_view()),
    path("students/<str:pk>/", views.StudentsAPIVIew.as_view()),
]
