from rest_framework import serializers
from .models import MenuSection, MenuColumn, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    to = serializers.CharField(source='link') # Map 'link' to 'to' for frontend
    
    class Meta:
        model = MenuItem
        fields = ['title', 'to']

class MenuColumnSerializer(serializers.ModelSerializer):
    innerTittle = serializers.CharField(source='title') # Map 'title' to 'innerTittle'
    childernlistL = MenuItemSerializer(source='items', many=True) # Map 'items' to 'childernlistL'

    class Meta:
        model = MenuColumn
        fields = ['innerTittle', 'childernlistL']

class MenuSectionSerializer(serializers.ModelSerializer):
    content = MenuColumnSerializer(source='columns', many=True) # Map 'columns' to 'content'

    class Meta:
        model = MenuSection
        fields = ['title', 'content']
