from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    """Purpose of slug:
        Makes clean, readable URLs instead of using IDs
        Example: /blog/my-blog-post/ instead of /blog/123/
        Better for SEO (search engines)
        Easier for users to read and remember
    """
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #table name, default ordering, permissions
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    #Tells Django how to display this object in admin/dropdowns    
    def __str__(self):
        return self.name
    
class product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True) #to pass it, if options occurs, select 1 and type "TEMP-SKU"
    product_stock = models.IntegerField()
    product_discount = models.IntegerField(default=0)

    #boolean field to check if the product is active or not
    is_active = models.BooleanField(default=True)

    #choice field
    STATUS_CHOICES = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
        ('discontinued', 'Discontinued'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_stock')

    #foreign key to category
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='products')
        # Delete related objects
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        # Set to NULL (requires null=True)
        # ForeignKey fields (automatic index added)

    #Date fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            # Database uses index to jump directly to matching rows
            models.Index(fields=['product_name']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"{self.product_name} - ${self.product_price}"
    
    @property
    #Creates a method that can be accessed like an attribute (without parentheses).
    def formatted_price(self):
        return f"PKR{self.product_price}"

class ProductImage(models.Model):
    """One-to-Many relationship with Product"""
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.product_name}"

class ProductSpecification(models.Model):
    """ One-to-One relationship with Product """
    product = models.OneToOneField(product, on_delete=models.CASCADE, related_name='specs')
    weight = models.FloatField()
    dimensions = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"Specs for {self.product.product_name}"
    

