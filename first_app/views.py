from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def myname(request):
    return HttpResponse('Hello Me!')
#    return render(request, 'first_app/mypage.html', {'name': 'Naveed'})

def yourname(request):
    return HttpResponse('Hello You!')


