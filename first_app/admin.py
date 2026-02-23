from django.contrib import admin

# Register your models here.

# first_app/admin.py
from .models import Category, BlogPost, PostDetail

admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(PostDetail)
