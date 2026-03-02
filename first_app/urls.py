from django.urls import path
from . import views #(to call the views.py file from the same directory)
urlpatterns = [
#	path('', views.home) # ‘’ it means, if path is empty so go to “def home(request):” of views.py
	path('home/', views.home, name='home'), # ‘’ it means, if path is empty so go to “def home(request):” of views.py
    path('student_signup/', views.student_signup_view, name='student_signup'),
    path('students/', views.student_list, name='student_list'),
    path('teacher_signup/', views.teacher_signup_view, name='teacher_signup'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('study_material/', views.study_material, name='study_material'),
]