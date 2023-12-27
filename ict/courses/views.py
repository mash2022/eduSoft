from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *
from reportlab.pdfgen import canvas

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
   custom_settings=CustomSettings.objects.all()
   context={
      'course':myCourses,
      'custom_settings':custom_settings,
   }
   return HttpResponse(template.render(context, request))

def teachers(request):
   teacher=Teacher.objects.all()
   custom_settings=CustomSettings.objects.all()
   context={
      'teacher':teacher,
      'custom_settings':custom_settings,
   }
   template=loader.get_template('teachers.html')
   return HttpResponse(template.render(context, request))

def about(request):
   template = loader.get_template('about.html')
   about = About.objects.all()
   custom_settings=CustomSettings.objects.all()
   context = {
      'about': about,
      'custom_settings':custom_settings,
   }
   return HttpResponse(template.render(context, request))

def events(request):
   #template=loader.get_template('events.html')
   data = Image.objects.all()
   custom_settings=CustomSettings.objects.all()
   context = {
      'data' : data,
      'custom_settings':custom_settings,
   }
   #return HttpResponse(template.render(context, request))
   return render(request,"events.html", context)

def admission(request):
   template=loader.get_template('admission.html')
   data=Admission.objects.all()
   custom_settings=CustomSettings.objects.all()
   context={
      'data':data,
      'custom_settings':custom_settings,
   }
   return HttpResponse(template.render(context, request))

def contact(request):
   form=ContactForm()
   custom_settings=CustomSettings.objects.all()
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
  student_count=AdmissionForm.objects.all().count()
  custom_settings_data=CustomSettings.objects.all()
  my_video=MyVideo.objects.all()
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

def admission_form(request):
   form=Admission_form()
   context={
      'form':form
   }
   template=loader.get_template('admission_form.html')
   return HttpResponse(template.render(context, request))

def admission_submit(request):
   form=Admission_form()  
   if request.method == 'POST':
      form=Admission_form(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('admission_form')
      else:
         return HttpResponse('Something wrong!')
   context={'form':form}
   return render(request, 'admission_form.html', context)

def student_list(request):
    student_list=AdmissionForm.objects.all()
    template=loader.get_template('student_list.html')
    context={
        'student_list':student_list
    }
    return HttpResponse(template.render(context, request))

def student_details(request, id):
  student_details = AdmissionForm.objects.get(id=id)
  template = loader.get_template('student_details.html')
  context = {
    'student_details': student_details,
  }
  return HttpResponse(template.render(context, request))

def studentInfo(request):
   form=StudentInfoForm()
   context={
      'form':form
   }
   template=loader.get_template('studentInfo.html')
   return HttpResponse(template.render(context, request))
  
def studentInfoUpload(request):
   if request.method=='POST':
      form=StudentInfoForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('paymentAdmission')
   else:
      form=StudentInfoForm()
      return HttpResponse(request, 'studentInfo.html', {'form':StudentInfoForm})
   
def paymentAdmission(request):
   form=PaymentAdmissionForm()
   context={
      'form':form
   }
   template=loader.get_template('paymentAdmission.html')
   return HttpResponse(template.render(context, request))

def paymentAdmissionSubmit(request):
   if request.method=='POST':
      form=PaymentAdmissionForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('studentProfile')
   else:
      form=PaymentAdmissionForm()
      return HttpResponse(request, 'paymentAdmission.html', {'form':StudentInfoForm}) 

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

# def signUp(request):
#    if request.method=='POST':
#       form=SignUpForm(request.POST, request.FILES)
#       if form.is_valid():
#          form.save()
#          return redirect('login')
#    else:
#       form=SignUpForm()
#       return HttpResponse(request, 'signUp.html', {'form':SignUpForm}) 
