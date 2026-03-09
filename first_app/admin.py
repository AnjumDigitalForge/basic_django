from django.contrib import admin # This line imports the admin module from django.contrib, which is used to register models with the Django admin site. By registering a model with the admin site, you can manage the data for that model through a user-friendly interface provided by Django.

from .models import StdSignUp, TeacherSignUp
from first_app import models # This line imports the std_sign_up model from the current app's models.py file. This allows you to use the std_sign_up model in this file, such as registering it with the admin site or performing database operations on it.

@admin.register(StdSignUp) # This line registers the std_sign_up model with the Django admin site. By doing this, you can manage the data for the std_sign_up model through the admin interface, allowing you to add, edit, and delete instances of std_sign_up easily.
class StdSignUpAdmin(admin.ModelAdmin):
    list_display = ['std_name', 'std_father_name', 'std_age', 'std_gender', 'std_grade', 'std_contact', 'std_email']
    list_filter = ['std_gender', 'std_grade']
    search_fields = ['std_name', 'std_father_name', 'std_email']
    list_per_page = 50

@admin.register(TeacherSignUp) # This line registers the teacher_sign_up model with the Django admin site. By doing this, you can manage the data for the teacher_sign_up model through the admin interface, allowing you to add, edit, and delete instances of teacher_sign_up easily.
class TeacherSignUpAdmin(admin.ModelAdmin):
    list_display = ['teacher_name', 'teacher_father_name', 'teacher_cnic', 'teacher_qualification', 'teacher_contact', 'teacher_address', 'teacher_email']
    list_filter = ['teacher_qualification']
    search_fields = ['teacher_name', 'teacher_father_name', 'teacher_email']
    list_per_page = 50
