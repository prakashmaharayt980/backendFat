from rest_framework import serializers
from products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_children(self, obj):
        return CategorySerializer(obj.children.all(), many=True).data