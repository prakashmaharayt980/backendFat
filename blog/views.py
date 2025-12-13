from rest_framework import viewsets, permissions, pagination
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostListSerializer, BlogPaginationSerializer

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'meta': {
                'current_page': self.page.number,
                'last_page': self.page.paginator.num_pages,
                'per_page': self.page_size,
                'total': self.page.paginator.count
            }
        })

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(is_published=True).order_by('-published_at')
    serializer_class = BlogPostListSerializer
    pagination_class = CustomPagination
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
