# from rest_framework import viewsets, filters, permissions
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Product, Category, Brand
# from .serializers import ProductListSerializer, ProductDetailSerializer, CategorySerializer, BrandSerializer
# from rest_framework.decorators import action
# from rest_framework.response import Response

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['category__slug', 'brand__slug', 'emi_enabled', 'slug']
#     search_fields = ['name', 'description']
#     ordering_fields = ['price', 'created_at']
#     lookup_field = 'slug'

#     def get_serializer_class(self):
#         if self.action == 'retrieve':
#             return ProductDetailSerializer
#         return ProductListSerializer

#     # Custom action to match specific frontend requests if needed, e.g. trending
#     @action(detail=False, methods=['get'])
#     def trending(self, request):
#         trending_products = self.queryset.filter(highlights__icontains='trending')[:5]
#         serializer = ProductListSerializer(trending_products, many=True)
#         return Response(serializer.data)

# class CategoryViewSet(viewsets.ModelViewSet):
#     # Modified to allow filtering by slug directly in list if needed or just return all roots
#     queryset = Category.objects.filter(parent=None) 
#     serializer_class = CategorySerializer
#     lookup_field = 'slug'

# class BrandViewSet(viewsets.ModelViewSet):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#     lookup_field = 'slug'


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import (
    Brand, Category, Product, ProductImage, ProductVariant
)
from .serializers import (
    BrandSerializer, CategorySerializer,
    ProductSerializer, ProductImageSerializer,
    ProductVariantSerializer
)

from rest_framework.permissions import AllowAny


# --------------------
# BRAND CRUD
# --------------------
class BrandAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            brand = get_object_or_404(Brand, pk=pk)
            return Response(BrandSerializer(brand).data)
        brands = Brand.objects.all()
        return Response(BrandSerializer(brands, many=True).data)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        serializer = BrandSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryAPIView(APIView):

    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category, pk=pk)
            return Response(CategorySerializer(category).data)
        categories = Category.objects.filter(parent__isnull=True)
        return Response(CategorySerializer(categories, many=True).data)

    def post(self, request):
        print("INside view")
        print(request.data)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductAPIView(APIView):


    def get(self, request, pk=None):
        if pk:
            product = get_object_or_404(Product, pk=pk)
            return Response(ProductSerializer(product).data)
        products = Product.objects.select_related('brand', 'category')
        return Response(ProductSerializer(products, many=True).data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductImageAPIView(APIView):


    def post(self, request):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        image = get_object_or_404(ProductImage, pk=pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductVariantAPIView(APIView):


    def post(self, request):
        serializer = ProductVariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        variant = get_object_or_404(ProductVariant, pk=pk)
        serializer = ProductVariantSerializer(variant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        variant = get_object_or_404(ProductVariant, pk=pk)
        variant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

