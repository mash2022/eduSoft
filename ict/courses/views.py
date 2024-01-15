from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse_lazy
from .models import *
from .forms import *
from reportlab.pdfgen import canvas
from django.contrib import messages

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
   context = {
      'about': about,
      'custom_settings':custom_settings,
      'course_count':course_count,
      'event_count':event_count,
      'trainer_count':trainer_count,
      'student_count':student_count,
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
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system #################################### 
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ################################################################## 
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'})

def login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form, 'title':'log in'})