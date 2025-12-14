# from rest_framework import serializers
# from .models import Product, Category, Brand, ProductVariant, ProductImage

# # Helper to match frontend image structure
# class FrontendImageSerializer(serializers.Serializer):
#     def to_representation(self, instance):
#         if not instance:
#             return None
#         url = instance.url if hasattr(instance, 'url') else instance
#         return {
#             "name": "default",
#             "default": url,
#             "original": url,
#             "preview": url,
#             "thumbnail": url,
#             "is_default": True
#         }

# class BrandSerializer(serializers.ModelSerializer):
#     brand_image = serializers.SerializerMethodField()

#     class Meta:
#         model = Brand
#         fields = ['id', 'name', 'slug', 'status', 'brand_image']

#     def get_brand_image(self, obj):
#         url = obj.image.url if obj.image else ""
#         return {"full": url, "thumb": url}

# class CategorySerializer(serializers.ModelSerializer):
#     image = FrontendImageSerializer()
#     children = serializers.SerializerMethodField()
#     parent_tree = serializers.SerializerMethodField()

#     class Meta:
#         model = Category
#         fields = ['id', 'title', 'slug', 'parent', 'parent_tree', 'children', 'image', 'description', 'meta_title', 'meta_description', 'meta_keywords', 'navbar_link', 'created_at', 'updated_at']

#     def get_children(self, obj):
#         # Avoid recursion depth issues or heavy loads. 
#         # For simplicity, we might not nest indefinitely here unless needed.
#         # Frontend likely expects direct children.
#         children = obj.children.all()
#         return CategorySerializer(children, many=True).data

#     def get_parent_tree(self, obj):
#         # Simple implementation
#         if obj.parent:
#             return f"{obj.parent.slug}/{obj.slug}"
#         return obj.slug

# class ProductListSerializer(serializers.ModelSerializer):
#     """
#     Matches `products.data` array in `CategorySlug` interface
#     """
#     image = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Product
#         fields = ['slug', 'highlights', 'emi_enabled', 'image', 'discounted_price', 'price', 'name']

#     def get_image(self, obj):
#         return obj.image.url if obj.image else ""

# class ProductDetailSerializer(serializers.ModelSerializer):
#     """
#     Matches `ProductDetails` interface
#     """
#     brand = BrandSerializer()
#     image = serializers.SerializerMethodField()
#     categories = serializers.SerializerMethodField()
#     variants = serializers.SerializerMethodField()
#     discountcampaign = serializers.SerializerMethodField()
#     attributes = serializers.DictField(default=dict)
#     average_rating = serializers.FloatField(default=0.0)
#     quantity = serializers.IntegerField(source='stock_quantity')
#     pre_order = serializers.IntegerField(default=0)
#     pre_order_price = serializers.FloatField(default=None)

#     class Meta:
#         model = Product
#         fields = [
#             'id', 'name', 'slug', 'price', 'pre_order', 'pre_order_price', 'quantity', 'discounted_price',
#             'emi_enabled', 'brand', 'image', 'reviews', 'highlights', 'attributes', 'average_rating',
#             'categories', 'variants', 'discountcampaign'
#         ]

#     def get_image(self, obj):
#          return obj.image.url if obj.image else ""

#     def get_categories(self, obj):
#         # Frontend expects array of categories (e.g. breadcrumbs or just the main one)
#         # We'll return the main category + its parents if needed. For now just the main one formatted.
#         cat = obj.category
#         return [{
#             "id": cat.id,
#             "title": cat.title,
#             "slug": cat.slug,
#             "image": {"full": cat.image.url, "thumb": cat.image.url, "preview": cat.image.url} if cat.image else {}
#         }]

#     def get_variants(self, obj):
#         # Transform variants to frontend expectation
#         return [{
#             "id": v.id,
#             "product_id": v.product.id,
#             "quantity": v.stock_quantity,
#             "price": v.price if v.price else obj.price,
#             "attributes": v.attributes,
#             "created_at": str(obj.created_at), # dummy
#             "updated_at": str(obj.updated_at), # dummy
#             "storage": v.attributes.get("Storage")
#         } for v in obj.variants.all()]

#     def get_discountcampaign(self, obj):
#         return None # Placeholder




# --------------------
# CATEGORY
# --------------------



# --------------------
