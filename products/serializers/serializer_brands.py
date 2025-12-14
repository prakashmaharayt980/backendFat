
from rest_framework import serializers
from products.models import Brand
# --------------------
# BRAND
# --------------------
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'