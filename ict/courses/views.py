from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Course

# Create your views here.
def courses(request):
    myCourses=Course.objects.all().values()
    template=loader.get_template('all_courses.html')
    context={
        'myCourses':myCourses
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  myCourses = Course.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myCourses': myCourses,
  }
  return HttpResponse(template.render(context, request))

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())