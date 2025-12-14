
from rest_framework import serializers
from products.models import Product,ProductImage,ProductVariant
# PRODUCT IMAGE
# --------------------
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


# --------------------
# PRODUCT VARIANT
# --------------------
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'


# --------------------
# PRODUCT
# --------------------
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
