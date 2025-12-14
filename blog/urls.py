from django.urls import path
from .views import BlogPostAPIView

urlpatterns = [
    path('blog', BlogPostAPIView.as_view()),
    path('blog/<int:pk>/', BlogPostAPIView.as_view()),
]
