from django.urls import path
from . import views

urlpatterns = [

    # =====================
    # BLOG POSTS
    # =====================
    path('blogs/', views.GetAllBlogPostsAPIView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', views.GetBlogPostByIdAPIView.as_view(), name='blog-detail'),
    path('blog/create/', views.CreateBlogPostAPIView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update/', views.UpdateBlogPostAPIView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', views.DeleteBlogPostAPIView.as_view(), name='blog-delete'),
]
