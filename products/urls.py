from django.urls import path
from .views import *

urlpatterns = [
    path('brands/', BrandAPIView.as_view(),name='get-brands'),
    path('brands/<int:pk>/', BrandAPIView.as_view(),name='create-brands'),

    path('categories', CategoryAPIView.as_view(),name='get-categories'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(),name='create-categories'),

    path('products/', ProductAPIView.as_view(),name='get-products'),
    path('products/<int:pk>/', ProductAPIView.as_view(),name='create-products'),

    path('product-images/', ProductImageAPIView.as_view(),name='get-product-images'),
    path('product-images/<int:pk>/', ProductImageAPIView.as_view(),name='create-product-images'),

    path('product-variants/', ProductVariantAPIView.as_view(),name='get-product-variants'),
    path('product-variants/<int:pk>/', ProductVariantAPIView.as_view(),name='create-product-variants'),
]
