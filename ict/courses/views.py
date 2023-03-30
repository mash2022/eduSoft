from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Course, Event
from. models import Teacher

# Create your views here.
def courses(request):
    myCourses=Course.objects.all().values()
    template=loader.get_template('all_courses.html')
    context={
        'myCourses':myCourses
    }
    return HttpResponse(template.render(context, request))

def courses2(request):
   myCourses = Course.objects.all().values()
   template=loader.get_template('courses.html')
   context={
      'course':myCourses
   }
   return HttpResponse(template.render(context, request))

def teachers(request):
   teacher=Teacher.objects.all()
   context={
      'teacher':teacher
   }
   template=loader.get_template('teachers.html')
   return HttpResponse(template.render(context, request))

def about(request):
   template=loader.get_template('about.html')
   return HttpResponse(template.render())

def events(request):
   template=loader.get_template('events.html')
   data = Event.objects.all()
   context = {
      'data' : data
   }
   return HttpResponse(template.render(context, request))

def admission(request):
   template=loader.get_template('admission.html')
   return HttpResponse(template.render())

def contact(request):
   template=loader.get_template('contact.html')
   return HttpResponse(template.render())

def details(request, id):
  myCourses = Course.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myCourses': myCourses,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
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
   