from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from .models import *
from .forms import *
from reportlab.pdfgen import canvas
from django.contrib import messages
# from django.template.loader import get_template
# from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import re
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import login as auth_login

# Create your views here.
def all_courses(request):
    my_courses=Course.objects.all()
    template=loader.get_template('courses.html')
    custom_settings = CustomSettings.objects.all()[1:]
    context={
        'course':my_courses,
        'custom_settings': custom_settings,
    }
    return HttpResponse(template.render(context, request))

def courses(request):
   my_courses = Course.objects.all()
   template=loader.get_template('courses.html')
   custom_settings = CustomSettings.objects.all()[1:]
   context={
      'course':my_courses,
      'custom_settings': custom_settings,
   }
   return HttpResponse(template.render(context, request))

def teachers(request):
   teacher=Teacher.objects.all()
   custom_settings=CustomSettings.objects.all()[1:]
   context={
      'teacher':teacher,
      'custom_settings':custom_settings,
   }
   template=loader.get_template('teachers.html')
   return HttpResponse(template.render(context, request))

def about(request):
   template = loader.get_template('about.html')
   about = About.objects.all()
   custom_settings=CustomSettings.objects.all()[1:]
   course_count=Course.objects.all().count()
   event_count=Event.objects.all().count()
   trainer_count=Teacher.objects.all().count()
   student_count=StudentInfo.objects.all().count()
   committee=Committee.objects.all()
   context = {
      'about': about,
      'custom_settings':custom_settings,
      'course_count':course_count,
      'event_count':event_count,
      'trainer_count':trainer_count,
      'student_count':student_count,
      'committee':committee,
   }
   return HttpResponse(template.render(context, request))

def events(request):
   template=loader.get_template('events.html')
   event_data = Event.objects.all()
   custom_settings = CustomSettings.objects.all()[1:]
   context = {
      'event_data' : event_data,
      'custom_settings':custom_settings,
   }
   return HttpResponse(template.render(context, request))

def admission_notice(request):
   template=loader.get_template('admission_notice.html')
   data=AdmissionNotice.objects.all()
   custom_settings = CustomSettings.objects.all()[1:]
   context={
      'data':data,
      'custom_settings':custom_settings,
   }
   return HttpResponse(template.render(context, request))

def contact(request):
   form=ContactForm()
   custom_settings=CustomSettings.objects.all()[1:]
   context={
      'form':form,
      'custom_settings':custom_settings,
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

def index(request):
  template = loader.get_template('index.html')
  data=Image.objects.all()
  notice_data=Notice.objects.all().reverse()[:2]
  course_data=Course.objects.all()
  course_count=Course.objects.all().count()
  event_count=Event.objects.all().count()
  trainer_count=Teacher.objects.all().count()
  trainer_data=Teacher.objects.all()
  student_count=StudentInfo.objects.all().count()
  custom_settings_data=CustomSettings.objects.all()[1:]
  my_video=MyVideo.objects.all()
  committee_member=Committee.objects.all()
  context={
     'data':data,
     'notice_data':notice_data,
     'course_data':course_data,
     'course_count':course_count,
     'event_count':event_count,
     'trainer_count':trainer_count,
     'trainer_data':trainer_data,
     'student_count':student_count,
     'custom_settings':custom_settings_data,
     'my_video':my_video,
     'committee_member':committee_member,
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
   return render(request, 'main.html', context)

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

def student_list(request):
    student_list=StudentInfo.objects.all()
    template=loader.get_template('student_list.html')
    context={
        'student_list':student_list
    }
    return HttpResponse(template.render(context, request))

def student_details(request, id):
  student_details = StudentInfo.objects.get(id=id)
  template = loader.get_template('student_details.html')
  context = {
    'student_details': student_details,
  }
  return HttpResponse(template.render(context, request))

def studentInfo(request):
   form=StudentInfoForm()
   custom_settings=CustomSettings.objects.all()[1:]
   context={
      'form':form,
      'custom_settings':custom_settings,
   }
   template=loader.get_template('studentInfo.html')
   return HttpResponse(template.render(context, request))
  
def studentInfoUpload(request):
   if request.method == 'POST':
      form=StudentInfoForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         messages.success(request, 'Successfully submited')
         return redirect('studentProfile')
      else:
         messages.error(request, 'Invalid data ! Try again.')
         return redirect('studentInfo')
   else:
      form=StudentInfoForm()
   return render(request, 'studentInfo.html',{'form':form})
   
def studentProfile(request):
   data=StudentInfo.objects.all()
   context={
      'data':data,
   }
   template=loader.get_template('student_signup.html')
   return HttpResponse(template.render(context, request))

def getPdf(request):
   response=HttpResponse(content_type='application/pdf')
   response['Content-deposition'] = 'attachment; filename="file.pdf"'
   p=canvas.Canvas(response)
   p.setFont('Times-Roman', 55)
   p.drawString(100, 700, 'ahasan')
   p.showPage()
   p.save()
   return response

def generate_pdf_file():
    from io import BytesIO
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    # Create a PDF document
    books = StudentInfo.objects.all()
    p.drawString(100, 750, "Student Info")
    y = 700
    for x in StudentInfo:
        p.drawString(100, y, f"Title: {x.name}")
        p.drawString(100, y - 20, f"Author: {x.fatherName}")
        p.drawString(100, y - 40, f"Year: {x.mobile}")
        y -= 60
 
    p.showPage()
    p.save()
 
    buffer.seek(0)
    return buffer

def circular(request):
   circular_data=Circular.objects.all()
   context={
      'circular_data':circular_data
   }
   return render(request, 'circular.html', context)

def signup(request):
      if request.method == 'POST':
         fname = request.POST['fname']
         lname = request.POST['lname']
         getname = fname +""+lname
         joinname ="".join(getname)
         repname = joinname.replace('.', '')
         cleandata = re.sub(r"\s+", "", repname)
         uname = cleandata

         email = request.POST['email']
         password = request.POST['psswrd']
         compass = request.POST['compasswrd']
         utype = request.POST['utype']

         error_message = None
         if password == compass:
               if Custom_User.objects.filter(email = email):
                  error_message = "Email Address already registered!"
                  context = {
                     'errormessage': error_message,
                  }
                  return render(request,'signup.html', context)
               else:
                  if not error_message:
                     customuser = Custom_User.objects.create(first_name=fname, last_name=lname, user_name=uname, email=email, password=make_password(compass), user_type=utype, is_active=True, is_staff=True)
                     customuser.save()
                     messages.success(request, f"User {customuser.user_name} Registration Successfully!")
                     return redirect('login')
      return render(request, 'signup.html')

def login(request):
    if request.customuser.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            custom_user = authenticate(email=email, password=password)
            if custom_user is not None:
                auth_login(request, custom_user)
                return redirect('dashboard')
            else:
                messages.error(request, f"Wrong username or password!")
                return redirect('login')     
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def log_out(request):
    logout(request)
    return redirect('index')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				auth_login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login1.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")
