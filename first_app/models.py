# BUILT-IN: Django's database tools
from django.db import models
# BUILT-IN: Django's user system
from django.contrib.auth.models import User

class std_sign_up(models.Model):
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    grade = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE) #Relationship field
    
    def __str__(self): #This method is used to return a string representation of the object. It is called when you print an instance of the model or when you display it in the Django admin interface.
        return self.student_name
    
    class Meta:
        verbose_name = 'Student Sign Up'        # Singular name in replacement of 'std_sign_up' the class / model name
        verbose_name_plural = 'Student Sign Ups' # Plural name in replacement of 'std_sign_up' the class / model name