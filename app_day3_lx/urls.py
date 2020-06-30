from django.urls import path

from app_day3_lx import views

urlpatterns = [
    path("books/", views.BookAPIView.as_view()),
    path("books/<str:id>/", views.BookAPIView.as_view()),

    path("books1/", views.BookAPIViewV2.as_view()),
    path("books2/<str:id>/", views.BookAPIViewV2.as_view()),
]
