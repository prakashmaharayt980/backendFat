from products.exceptions import BaseAPIView
from rest_framework.response import Response
from products.serializers import BrandSerializer
from rest_framework import status
from products.models import Brand
from django.shortcuts import get_object_or_404


class CreateBrandAPIView(BaseAPIView):
    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetAllBrandAPIView(BaseAPIView):
    def get(self, request):
        brands = Brand.objects.all()
        return Response(BrandSerializer(brands, many=True).data)


class GetBrandByIdAPIView(BaseAPIView):
    def get(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        return Response(BrandSerializer(brand).data)

class UpdateBrandAPIView(BaseAPIView):
    def put(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        serializer = BrandSerializer(brand, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DeleteBrandAPIView(BaseAPIView):
    def delete(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)