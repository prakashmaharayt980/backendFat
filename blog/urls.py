from django.urls import path
from .views import BlogPostAPIView

urlpatterns = [
    path('', BlogPostAPIView.as_view()),
    path('<int:pk>/', BlogPostAPIView.as_view()),
]
