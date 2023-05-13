from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import *

# Create your views here.
def all_courses(request):
    myCourses=Course.objects.all()
    template=loader.get_template('courses.html')
    context={
        'course':myCourses
    }
    return HttpResponse(template.render(context, request))

def courses(request):
   myCourses = Course.objects.all()
   template=loader.get_template('courses.html')
   course_count=Course.objects.all().count()
   context={
      'course':myCourses,
      'course_count':course_count,
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
   template = loader.get_template('about.html')
   about = About.objects.all()
   context = {
      'about': about
   }
   return HttpResponse(template.render(context, request))

def events(request):
   #template=loader.get_template('events.html')
   data = Image.objects.all()
   context = {
      'data' : data
   }
   #return HttpResponse(template.render(context, request))
   return render(request,"events.html", context)

def admission(request):
   template=loader.get_template('admission.html')
   data=Admission.objects.all()
   context={
      'data':data
   }
   return HttpResponse(template.render(context, request))

def contact(request):
   form=ContactForm()
   context={
      'form':form
   }
   template=loader.get_template('contact.html')
   return HttpResponse(template.render(context, request))

def details(request, id):
  myCourses = Course.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myCourses': myCourses,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  data=Image.objects.all()
  notice_data=Notice.objects.all()
  course_data=Course.objects.all()
  context={
     'data':data,
     'notice_data':notice_data,
     'course_data':course_data,
  }
  return HttpResponse(template.render(context, request))

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

def image(request):
   data=Image.objects.all()
   context={
      'data':data
   }
   return render(request, main.html, context)

def uploadImage(request):
   if request.method=='POST':
      form=ImageUploadForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('contact')
      
   else:
      form=ImageUploadForm()
   return render(request, 'contact.html', {'form':form})

def contactUpload(request):
   if request.method=='POST':
      form=ContactForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('contact')
   else:
      form=ContactForm()
      return HttpResponse(request, 'contact.html', {'form':ContactForm})

def admission_form(request):
   form=Admission_form()
   context={
      'form':form
   }
   template=loader.get_template('admission_form.html')
   return HttpResponse(template.render(context, request))

def admission_submit(request):
   if request.method=='POST':
      form=Admission_form(request.POST)
      if form.is_valid():
         form.save()
         return redirect('admission_form')
      form=Admission_form()
      return render(request, 'admission_form.html', {'form':form})
