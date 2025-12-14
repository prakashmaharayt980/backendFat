from products.exceptions import BaseAPIView
from rest_framework.response import Response
from rest_framework import status
from products.serializers import CategorySerializer
from products.models import Category
from django.shortcuts import get_object_or_404
from products.pagination import ProductsPagination

class CreateCategoryAPIView(BaseAPIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class GetAllCategoryAPIView(BaseAPIView):
    def get(self, request):
        categories = Category.objects.filter(parent__isnull=True)
        paginator = ProductsPagination()
        page = paginator.paginate_queryset(categories,request)
        serializer = CategorySerializer(page,many=True)
        return paginator.get_paginated_response(serializer.data)


class GetCategoryByIdAPIView(BaseAPIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        return Response(CategorySerializer(category).data)


class UpdateCategoryAPIView(BaseAPIView):
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeleteCategoryAPIView(BaseAPIView):
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)