from urllib import request

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def myname(request):
    return HttpResponse('Hello Me!')
#    return render(request, 'first_app/mypage.html', {'name': 'Naveed'})

def yourname(request):
    return HttpResponse('Hello You!')

def enrolled_students(request):
    return HttpResponse('Enrolled Students')

def sign_up(request):
    return render(request, 'std_sign_up.html')  # This finds your template

