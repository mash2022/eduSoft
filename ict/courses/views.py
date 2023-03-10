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

def testing(request):
   mySearchData=Course.objects.filter(course_name='DBMS', id=2).values()
   myData=Course.objects.all()
   myGetData=Course.objects.all().values()
   template=loader.get_template('template.html')
   context={
      'fruits':['apple', 'banana', 'cherry'],
      'course_name':'DBMS',
      'greeting':1,
      'myCourses':myData,
      'myGetValue':myGetData,
      'mySearchData':mySearchData,
   }
   return HttpResponse(template.render(context, request))
   