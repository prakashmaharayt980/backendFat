from django.db import models

class MenuSection(models.Model):
    """Top level menu items e.g. 'Laptops By Brands', 'Accessories'"""
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class MenuColumn(models.Model):
    """Inner columns e.g. 'Dell', 'Asus' under 'Laptops By Brands'"""
    section = models.ForeignKey(MenuSection, on_delete=models.CASCADE, related_name='columns')
    title = models.CharField(max_length=255) # "innerTittle" in json
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.section.title} > {self.title}"

class MenuItem(models.Model):
    """The actual links e.g. 'Inspiron Series'"""
    column = models.ForeignKey(MenuColumn, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=500) # "to" in json
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
