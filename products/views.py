


# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework import status
# # from django.shortcuts import get_object_or_404

# # from .models import (
# #     Brand, Category, Product, ProductImage, ProductVariant
# # )
# # from .serializers import (
# #     BrandSerializer, CategorySerializer,
# #     ProductSerializer, ProductImageSerializer,
# #     ProductVariantSerializer
# # )

# # from rest_framework.permissions import AllowAny


# # # --------------------
# # # BRAND CRUD
# # # --------------------
# # class BrandAPIView(APIView):

# #     def get(self, request, pk=None):
# #         if pk:
# #             brand = get_object_or_404(Brand, pk=pk)

# #             return Response(BrandSerializer(brand).data)
# #         brands = Brand.objects.all()
# #         return Response(BrandSerializer(brands, many=True).data)

# #     def post(self, request):
# #         serializer = BrandSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def put(self, request, pk):
# #         brand = get_object_or_404(Brand, pk=pk)
# #         serializer = BrandSerializer(brand, data=request.data, partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         brand = get_object_or_404(Brand, pk=pk)
# #         brand.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)



# # class CategoryAPIView(APIView):

# #     def get(self, request, pk=None):
# #         if pk:
# #             category = get_object_or_404(Category, pk=pk)
# #             return Response(CategorySerializer(category).data)
# #         categories = Category.objects.filter(parent__isnull=True)
# #         return Response(CategorySerializer(categories, many=True).data)

# #     def post(self, request):
# #         print("INside view")
# #         print(request.data)
# #         serializer = CategorySerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def put(self, request, pk):
# #         print(pk)
# #         category = get_object_or_404(Category, pk=pk)
# #         serializer = CategorySerializer(category, data=request.data, partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         category = get_object_or_404(Category, pk=pk)
# #         category.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)


# # class ProductAPIView(APIView):


# #     def get(self, request, pk=None):
# #         if pk:
# #             product = get_object_or_404(Product, pk=pk)
# #             return Response(ProductSerializer(product).data)
# #         products = Product.objects.select_related('brand', 'category')
# #         return Response(ProductSerializer(products, many=True).data)

# #     def post(self, request):
# #         serializer = ProductSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def put(self, request, pk):
# #         product = get_object_or_404(Product, pk=pk)
# #         serializer = ProductSerializer(product, data=request.data, partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         product = get_object_or_404(Product, pk=pk)
# #         product.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)


# # class ProductImageAPIView(APIView):


# #     def post(self, request):
# #         serializer = ProductImageSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         image = get_object_or_404(ProductImage, pk=pk)
# #         image.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)


# # class ProductVariantAPIView(APIView):


# #     def post(self, request):
# #         serializer = ProductVariantSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def put(self, request, pk):
# #         variant = get_object_or_404(ProductVariant, pk=pk)
# #         serializer = ProductVariantSerializer(variant, data=request.data, partial=True)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     def delete(self, request, pk):
# #         variant = get_object_or_404(ProductVariant, pk=pk)
# #         variant.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from django.db import DatabaseError, IntegrityError
# from rest_framework.exceptions import ValidationError
# from rest_framework.permissions import AllowAny

# from exceptions import BaseAPIView
# from .models import Brand, Category, Product
# from .serializers import (
#     BrandSerializer,
#     CategorySerializer,
#     ProductSerializer
# )


# class CreateCategoryAPIView(BaseAPIView):
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    


# class GetAllCategoryAPIView(BaseAPIView):
#     def get(self, request):
#         categories = Category.objects.filter(parent__isnull=True)
#         return Response(CategorySerializer(categories, many=True).data)


# class GetCategoryByIdAPIView(BaseAPIView):
#     def get(self, request, pk):
#         category = get_object_or_404(Category, pk=pk)
#         return Response(CategorySerializer(category).data)


# class UpdateCategoryAPIView(BaseAPIView):
#     def put(self, request, pk):
#         category = get_object_or_404(Category, pk=pk)
#         serializer = CategorySerializer(category, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# class DeleteCategoryAPIView(BaseAPIView):
#     def delete(self, request, pk):
#         category = get_object_or_404(Category, pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# # brands views

# class CreateBrandAPIView(BaseAPIView):
#     def post(self, request):
#         serializer = BrandSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class GetAllBrandAPIView(BaseAPIView):
#     def get(self, request):
#         brands = Brand.objects.all()
#         return Response(BrandSerializer(brands, many=True).data)


# class GetBrandByIdAPIView(BaseAPIView):
#     def get(self, request, pk):
#         brand = get_object_or_404(Brand, pk=pk)
#         return Response(BrandSerializer(brand).data)

# class UpdateBrandAPIView(BaseAPIView):
#     def put(self, request, pk):
#         brand = get_object_or_404(Brand, pk=pk)
#         serializer = BrandSerializer(brand, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# class DeleteBrandAPIView(BaseAPIView):
#     def delete(self, request, pk):
#         brand = get_object_or_404(Brand, pk=pk)
#         brand.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # products views

# class CreateProductAPIView(BaseAPIView):
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class GetAllProductAPIView(BaseAPIView):
#     def get(self, request):
#         products = Product.objects.select_related('brand', 'category')
#         return Response(ProductSerializer(products, many=True).data)
