
from django.contrib import admin
from . import models
from .models import category, product, ProductImage, ProductSpecification


# Register your models here.

#Alternative way to register (decorator syntax)
@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    #Controls how model appears in admin:
    list_display = ['name', 'slug', 'created_at']
    #As you type the title, the slug field fills itself!
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name']

@admin.register(product)
# when Need to customize admin display
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'product_stock', 'sku', 'status', 'created_at']
    list_filter = ['status', 'category', 'is_active'] #Adds filter sidebar
    search_fields = ['product_name', 'product_description'] #Adds search box
    list_editable = ['product_price', 'product_stock'] #Edit fields directly in list view
    readonly_fields = ['created_at', 'updated_at']
    
    """
        Why use it (fieldsets):
        Groups and organizes fields into sections in the admin add/edit form.
            1. Makes admin panel professional and organized
            2. Groups related fields (like pricing fields together)
            3. Hides advanced/debug fields behind collapsible sections
            4. Better for forms with 10+ fields
    """
    fieldsets = (
        ('Basic Information', {
            'fields': ('product_name', 'product_description', 'category')
        }),
        ('Pricing & Stock', {
            'fields': ('product_price', 'product_stock', 'is_active')
        }),
        ('Status', {
            'fields': ('status', 'created_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

# Quick registration (no customization)
admin.site.register(ProductImage)

admin.site.register(ProductSpecification)
