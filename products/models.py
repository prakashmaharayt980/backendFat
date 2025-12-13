from django.db import models
from django.utils.text import slugify

class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='brands/', null=True, blank=True)
    status = models.CharField(max_length=50, default='active')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    description = models.TextField(blank=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    navbar_link = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    description = models.TextField(blank=True)
    highlights = models.TextField(blank=True)
    specifications = models.JSONField(default=dict, blank=True)
    attributes = models.JSONField(default=dict, blank=True) # General attributes
    
    image = models.ImageField(upload_to='products/')
    
    emi_enabled = models.BooleanField(default=False)
    stock_quantity = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/gallery/')
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.name}"

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    attributes = models.JSONField() # e.g. {"Color": "Red", "Storage": "256GB"}
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # Override base price
    stock_quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/variants/', null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.attributes}"
