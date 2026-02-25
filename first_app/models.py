# BUILT-IN: Django's database tools
from django.db import models
# BUILT-IN: Django's user system
from django.contrib.auth.models import User

class std_sign_up(models.Model):
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#    def __str__(self):
#        return self.student_name