from django.db import models # BUILT-IN: Django's database tools

from django.contrib.auth.models import User # BUILT-IN: Django's user system

class StdSignUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students", blank=True, null=True)  # Establishes a foreign key relationship with the User model
    std_name = models.CharField(max_length=100)
    std_father_name = models.CharField(max_length=100)
    std_age = models.IntegerField()
    std_gender = models.CharField(max_length=10)
    std_grade = models.CharField(max_length=30)
    std_contact = models.CharField(max_length=15)
    std_email = models.EmailField()
    std_password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.std_name}"

class TeacherSignUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher", blank=True, null=True)  # Establishes a foreign key relationship with the User model
    teacher_name = models.CharField(max_length=100)
    teacher_father_name = models.CharField(max_length=100)
    teacher_cnic = models.IntegerField()
    teacher_qualification = models.CharField(max_length=50)
    teacher_contact = models.CharField(max_length=15)
    teacher_address = models.CharField(max_length=200, blank=True)
    teacher_email = models.EmailField()
    teacher_password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.teacher_name}"
