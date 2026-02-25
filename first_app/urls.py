from django.urls import path
from . import views #(to call the views.py file from the same directory)
urlpatterns = [
#	path('', views.home) # ‘’ it means, if path is empty so go to “def home(request):” of views.py
	path('myname/', views.myname),
	path('yourname/', views.yourname),
	path('students_list/', views.enrolled_students),
]