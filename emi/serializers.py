from rest_framework import serializers
from .models import EMIApplication, Bank
from products.serializers import ProductListSerializer

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class EMIApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMIApplication
        fields = '__all__'
        read_only_fields = ['application_no', 'status', 'applied_date', 'approved_date']

class EMIApplicationDetailSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    bank = BankSerializer(read_only=True)
    
    class Meta:
        model = EMIApplication
        fields = '__all__'
