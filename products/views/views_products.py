from products.exceptions import BaseAPIView
from rest_framework import status
from rest_framework.response import Response
from products.serializers import ProductSerializer,ProductImageSerializer,ProductVariantSerializer
from products.models import Product,ProductImage,ProductVariant
from django.shortcuts import get_object_or_404

class CreateProductAPIView(BaseAPIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetAllProductAPIView(BaseAPIView):
    def get(self, request):
        products = Product.objects.select_related('brand', 'category')
        return Response(ProductSerializer(products, many=True).data)


class GetProductByIdAPIView(BaseAPIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return Response(ProductSerializer(product).data)


class UpdateProductAPIView(BaseAPIView):
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeleteProductAPIView(BaseAPIView):
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CreateProductImageAPIView(BaseAPIView):
    def post(self, request):
        serializer = ProductImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetProductImagesByProductAPIView(BaseAPIView):
    def get(self, request, product_id):
        images = ProductImage.objects.filter(product_id=product_id)
        return Response(ProductImageSerializer(images, many=True).data)



class DeleteProductImageAPIView(BaseAPIView):
    def delete(self, request, pk):
        image = get_object_or_404(ProductImage, pk=pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateProductVariantAPIView(BaseAPIView):
    def post(self, request):
        serializer = ProductVariantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetVariantsByProductAPIView(BaseAPIView):
    def get(self, request, product_id):
        variants = ProductVariant.objects.filter(product_id=product_id)
        return Response(ProductVariantSerializer(variants, many=True).data)


class UpdateProductVariantAPIView(BaseAPIView):
    def put(self, request, pk):
        variant = get_object_or_404(ProductVariant, pk=pk)
        serializer = ProductVariantSerializer(variant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DeleteProductVariantAPIView(BaseAPIView):
    def delete(self, request, pk):
        variant = get_object_or_404(ProductVariant, pk=pk)
        variant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




