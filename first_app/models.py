# first_app/models.py
from django.db import models
from django.contrib.auth.models import User

# ----- CUSTOM MANAGER -----
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

# ----- CATEGORY MODEL -----
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

# ----- BLOG POST MODEL -----
class BlogPost(models.Model):
    # Fields
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    
    # Relationships
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    
    # Managers
    objects = models.Manager()  # Default
    published = PublishedManager()  # Custom
    
    # Meta
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
    
    def __str__(self):
        return self.title

# ----- POST DETAIL MODEL (OneToOne example) -----
class PostDetail(models.Model):
    post = models.OneToOneField(BlogPost, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Details for {self.post.title}"
