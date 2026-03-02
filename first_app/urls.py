from django.urls import path
from . import views #(to call the views.py file from the same directory)
urlpatterns = [
#	path('', views.home) # ‘’ it means, if path is empty so go to “def home(request):” of views.py
	path('myname/', views.myname),
	path('yourname/', views.yourname),
    path('signup/', views.signup_view, name='signup'),
    path('students/', views.student_list, name='student_list'),
]