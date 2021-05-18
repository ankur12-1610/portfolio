from main.models import Tutorial
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def myprojects(request):
    return render(request=request, 
                  template_name='myprojects.html',
                  context={"tutorials": Tutorial.objects.all})
