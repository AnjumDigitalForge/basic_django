from django.http import HttpResponse

from django.shortcuts import render, redirect # BUILT-IN: Django's tools for rendering templates and redirecting users to different pages

from .models import StdSignUp, TeacherSignUp # This line imports the std_sign_up model from the current app's models.py file. This allows you to use the std_sign_up model in this file, such as registering it with the admin site or performing database operations on it.

# Create your views here.
def home(request):
    return render(request, 'index.html')

def student_signup_view(request):
    if request.method == 'POST':
        # Get form data from the POST request
        StdSignUp.objects.create(
        std_name = request.POST['std_name'],
        std_father_name = request.POST['std_father_name'],
        std_age = request.POST['std_age'],
        std_gender = request.POST['std_gender'],
        std_grade = request.POST['std_grade'],
        std_contact = request.POST['std_contact'],
        std_email = request.POST['std_email'],
        )
        return redirect('students_dashboard')  # Redirect to a page that shows the list of students after successful registration
    return render(request, 'std_sign_up.html')  # Render the registration form template for GET requests

def student_list(request):
    students = StdSignUp.objects.all()  # Retrieve all student records from the database
    return render(request, 'enrolled_students.html', {'students': students})  # Render the student list template with the retrieved student data

def dashboard_std(request):
    return render(request, 'dashboard_std.html')  # Render the student dashboard template for GET requests

def teacher_signup_view(request):
    if request.method == 'POST':
        # Get form data from the POST request
        TeacherSignUp.objects.create(
        teacher_name = request.POST['teacher_name'],
        teacher_father_name = request.POST['teacher_father_name'],
        teacher_cnic = request.POST['teacher_cnic'],
        teacher_qualification = request.POST['teacher_qualification'],
        teacher_contact = request.POST['teacher_contact'],
        teacher_address = request.POST['teacher_address'],
        teacher_email = request.POST['teacher_email'],
        teacher_password = request.POST['teacher_password']
        )
        return redirect('teachers_dashboard')  # Redirect to a page that shows the list of teachers after successful registration
    return render(request, 'teacher_signup.html')  # Render the registration form template for GET requests

def dashboard_tch(request):
    return render(request, 'dashboard_tch.html')  # Render the teacher dashboard template for GET requests

def teacher_list(request):
    teachers = TeacherSignUp.objects.all()  # Retrieve all teacher records from the database
    return render(request, 'faculty_list.html', {'teachers': teachers})  # Render the teacher list template with the retrieved teacher data

def study_material(request):
    return render(request, 'stdy_material.html')  # Render the study material template for GET requests

def profile_std(request):
    return render(request, 'profile_std.html')  # Render the student profile template for GET requests

def profile_tchr(request):
    return render(request, 'profile_tchr.html')  # Render the teacher profile template for GET requests