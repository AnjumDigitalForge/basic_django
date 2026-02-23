from django.http import HttpResponse
from django.shortcuts import render

from first_app.models import BlogPost

# Create your views here.
def myname(request):
    return HttpResponse('Hello Me!')
#    return render(request, 'first_app/mypage.html', {'name': 'Naveed'})

def yourname(request):
    return HttpResponse('Hello You!')

def test_models(request):
    count = BlogPost.objects.count()
    return HttpResponse(f"Number of blog posts in database: {count}")