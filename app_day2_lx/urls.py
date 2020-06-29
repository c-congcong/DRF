from django.urls import path

from app_day2_lx import views

urlpatterns = [

    path("emp/", views.EmployeeAPIView.as_view()),
    path("emp/<str:id>/", views.EmployeeAPIView.as_view()),
]
