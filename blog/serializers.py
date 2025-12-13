from rest_framework import serializers
from .models import BlogPost
import math

class AuthorSerializer(serializers.Serializer):
    """
    Serializer to match frontend 'author' string expectation or object if needed.
    Frontend expects string name for now.
    """
    def to_representation(self, value):
        return value.username

class BlogPostListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S.%fZ")
    updated_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S.%fZ")
    
    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'content', 'created_at', 'slug', 'title', 'updated_at', 'image', 'category', 'read_time']

    def get_author(self, obj):
        return obj.author.fullname if obj.author.fullname else obj.author.email.split('@')[0]

class BlogPaginationSerializer(serializers.Serializer):
    """
    Custom serializer to format response exactly like `bloginfointerface`.
    """
    data = BlogPostListSerializer(many=True)
    meta = serializers.SerializerMethodField()

    def get_meta(self, obj):
        # Obj is the pagination object (Page)
        return {
            "current_page": obj.number,
            "last_page": obj.paginator.num_pages,
            "per_page": obj.paginator.per_page,
            "total": obj.paginator.count
        }
