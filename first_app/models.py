# BUILT-IN: Django's database tools
from django.db import models
# BUILT-IN: Django's user system
from django.contrib.auth.models import User

class PublishedManager(models.Manager): # WE CREATE: Custom query method
    # BUILT-IN: get_queryset() is Django's method to start a query
    def get_queryset(self): # WE OVERRIDE: Change how queries work
        # BUILT-IN: super().get_queryset() gets the default query
        # .filter(is_published=True) only gets published posts
        return super().get_queryset().filter(is_published=True) # WE ADD: Filter condition
    
# Purpose: Store categories like "Technology", "Food", "Travel"
class Category(models.Model): #WE CREATE: A new table called Category
    #BUILT-IN: models.CharField is a Django field type for text
    name = models.CharField(max_length=100) # WE CREATE: A column called 'name' that holds text
    
    class Meta: # WE CREATE: Extra settings for this model
        # BUILT-IN: verbose_name_plural is a Django option
        verbose_name_plural = 'Categories' # WE SET: In admin, show "Categories" not "Categorys"
    
    def __str__(self): # WE CREATE: A method to show this model as text
        return self.name # WE SET: When displayed, show the name field

class BlogPost(models.Model): # WE CREATE: A new table called BlogPost
    
    # ----- FIELDS (columns in database) -----
    # BUILT-IN: CharField = text with maximum length
    title = models.CharField(max_length=200) # WE CREATE: title column, max 200 chars
    
    # BUILT-IN: TextField = long text without max
    content = models.TextField() # WE CREATE: content column for long blog text
    
    # BUILT-IN: DateTimeField = date and time
    # auto_now_add=True = Django sets this automatically when created
    created_at = models.DateTimeField(auto_now_add=True) # WE CREATE: created_at column
    
    # BUILT-IN: BooleanField = True/False
    # default=False = starts as False
    is_published = models.BooleanField(default=False) # WE CREATE: published status column
    
    # ----- RELATIONSHIPS (connecting tables) -----
    # BUILT-IN: ForeignKey = links to another table
    # on_delete=models.CASCADE = if User deleted, delete their posts too
    author = models.ForeignKey(User, on_delete=models.CASCADE) # WE CREATE: link to User table
    
    # BUILT-IN: ManyToManyField = links many posts to many categories
    categories = models.ManyToManyField(Category) # WE CREATE: link to Category table
    
    # ----- MANAGERS (how to query the database) -----
    # BUILT-IN: Manager() = default way to get all objects
    objects = models.Manager() # WE USE: BlogPost.objects.all()
    
    # WE CREATE: Our custom manager (defined above)
    published = PublishedManager() # WE USE: BlogPost.published.all()
    
    # ----- META CLASS (table settings) -----
    class Meta: # WE CREATE: Extra settings
        # BUILT-IN: ordering = default sort order
        ordering = ['-created_at'] # WE SET: Newest posts first (- means descending)
        
        # BUILT-IN: verbose_name = singular name in admin
        verbose_name = 'Blog Post' # WE SET: In admin, show "Blog Post"
    
    # ----- STRING METHOD (how it appears) -----
    def __str__(self): # WE CREATE: Text representation
        return self.title # WE SET: Show title when printed
    
class PostDetail(models.Model): # WE CREATE: A new table called PostDetail
    
    # BUILT-IN: OneToOneField = each post has ONE detail record
    # on_delete=models.CASCADE = if post deleted, delete its details too
    post = models.OneToOneField(BlogPost, on_delete=models.CASCADE) # WE CREATE: link to BlogPost
    
    # BUILT-IN: IntegerField = whole number
    # default=0 = starts at 0
    views = models.IntegerField(default=0) # WE CREATE: views count column
    
    likes = models.IntegerField(default=0) # WE CREATE: likes count column
    
    def __str__(self): # WE CREATE: Text representation
        return f"Details for {self.post.title}" # WE SET: Show which post this belongs to

