from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("all_courses/", views.all_courses, name="all_courses"),
    path("teachers/", views.teachers, name="teachers"),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('image/', views.image, name='image'),
    path('admission/', views.admission, name='admission'),
    path('contact/', views.contact, name='contact'),
    path("courses/", views.courses, name="courses"),
    path('courses/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('uploadImage/', views.uploadImage, name='uploadImage'),
    path('contactUpload/', views.contactUpload, name='contactUpload'),
    path('admission_form/',views.admission_form, name='admission_form'),
    path('admission_submit/', views.admission_submit, name='admission_submit'),
    path("student_list/", views.student_list, name="student_list"),
    path('student_list/student_details/<int:id>', views.student_details, name='student_details'),
    path('studentInfo/', views.studentInfo, name='studentInfo'),
    path('studentInfoUpload/', views.studentInfoUpload, name='studentInfoUpload'),
    path('paymentAdmission/', views.paymentAdmission, name='paymentAdmission'),
    path('paymentAdmissionSubmit/', views.paymentAdmissionSubmit, name='paymentAdmissionSubmit'),
    path('studentProfile', views.studentProfile, name='studentProfile'),
    path('signUp', views.signUp, name='signUp'),

]
