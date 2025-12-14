
from django.urls import path
from products import views

urlpatterns = [

    # =====================
    # CATEGORY
    # =====================
    path('categories/', views.GetAllCategoryAPIView.as_view(), name='category-list'),
    path('category/create/', views.CreateCategoryAPIView.as_view(), name='category-create'),
    path('category/<int:pk>/', views.GetCategoryByIdAPIView.as_view(), name='category-detail'),
    path('category/<int:pk>/update/', views.UpdateCategoryAPIView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.DeleteCategoryAPIView.as_view(), name='category-delete'),

    # =====================
    # BRAND
    # =====================
    path('brands/', views.GetAllBrandAPIView.as_view(), name='brand-list'),
    path('brand/create/', views.CreateBrandAPIView.as_view(), name='brand-create'),
    path('brand/<int:pk>/', views.GetBrandByIdAPIView.as_view(), name='brand-detail'),
    path('brand/<int:pk>/update/', views.UpdateBrandAPIView.as_view(), name='brand-update'),
    path('brand/<int:pk>/delete/', views.DeleteBrandAPIView.as_view(), name='brand-delete'),

    # =====================
    # PRODUCT
    # =====================
    path('products/', views.GetAllProductAPIView.as_view(), name='product-list'),
    path('product/create/', views.CreateProductAPIView.as_view(), name='product-create'),
    path('product/<int:pk>/', views.GetProductByIdAPIView.as_view(), name='product-detail'),
    path('product/<int:pk>/update/', views.UpdateProductAPIView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.DeleteProductAPIView.as_view(), name='product-delete'),

    # =====================
    # PRODUCT IMAGES
    # =====================
    path('product-image/create/',views.CreateProductImageAPIView.as_view(),name='product-image-create'),
    path('product/<int:product_id>/images/',views.GetProductImagesByProductAPIView.as_view(),name='product-image-list'),
    path('product-image/<int:pk>/delete/', views.DeleteProductImageAPIView.as_view(), name='product-image-delete'),

    # =====================
    # PRODUCT VARIANTS
    # =====================
    path('product-variant/create/', views.CreateProductVariantAPIView.as_view(), name='product-variant-create'),
    path('product/<int:product_id>/variants/', views.GetVariantsByProductAPIView.as_view(), name='product-variant-list'),
    path('product-variant/<int:pk>/', views.GetVariantsByProductAPIView.as_view(), name='product-variant-detail'),
    path('product-variant/<int:pk>/update/', views.UpdateProductVariantAPIView.as_view(), name='product-variant-update'),
    path('product-variant/<int:pk>/delete/', views.DeleteProductVariantAPIView.as_view(), name='product-variant-delete'),

]
