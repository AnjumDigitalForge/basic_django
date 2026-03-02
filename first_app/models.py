from django.db import models # BUILT-IN: Django's database tools

from django.contrib.auth.models import User # BUILT-IN: Django's user system

class StdSignUp(models.Model):
    std_name = models.CharField(max_length=100)
    std_father_name = models.CharField(max_length=100)
    std_age = models.IntegerField()
    std_gender = models.CharField(max_length=10)
    std_grade = models.CharField(max_length=30)
    std_contact = models.CharField(max_length=15)
    std_email = models.EmailField()
    std_password = models.CharField(max_length=20)
    user = models.ManyToManyField(User, blank=True)  # Establishes a many-to-many relationship with the User model

    def __str__(self):
        return f"{self.id} - {self.std_name}"

class TeacherSignUp(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_father_name = models.CharField(max_length=100)
    teacher_age = models.IntegerField()
    teacher_qualification = models.CharField(max_length=50)
    teacher_contact = models.CharField(max_length=15)
    teacher_email = models.EmailField()
    teacher_password = models.CharField(max_length=20)
    user = models.ManyToManyField(User, blank=True)  # Establishes a many-to-many relationship with the User model

    def __str__(self):
        return f"{self.id} - {self.teacher_name}"
