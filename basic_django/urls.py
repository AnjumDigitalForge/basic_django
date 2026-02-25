"""
URL configuration for basic_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
#why does we have used ‘include’ here?

urlpatterns = [
    path('', lambda request: redirect('myname/')),  # Redirect root to myname/
    path('admin/', admin.site.urls),
	path('', include('first_app.urls')), #this will include the urls.py file of first_app and it will check the urls.py file of first_app for the path and views.
    
]

