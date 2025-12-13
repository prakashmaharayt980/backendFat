from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Category, Brand
from .serializers import ProductListSerializer, ProductDetailSerializer, CategorySerializer, BrandSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category__slug', 'brand__slug', 'emi_enabled', 'slug']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductListSerializer

    # Custom action to match specific frontend requests if needed, e.g. trending
    @action(detail=False, methods=['get'])
    def trending(self, request):
        trending_products = self.queryset.filter(highlights__icontains='trending')[:5]
        serializer = ProductListSerializer(trending_products, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    # Modified to allow filtering by slug directly in list if needed or just return all roots
    queryset = Category.objects.filter(parent=None) 
    serializer_class = CategorySerializer
    lookup_field = 'slug'

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'
