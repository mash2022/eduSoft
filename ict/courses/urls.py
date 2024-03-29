from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("all_courses/", views.all_courses, name="all_courses"),
    path("teachers/", views.teachers, name="teachers"),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('image/', views.image, name='image'),
    path('admission_notice/', views.admission_notice, name='admission_notice'),
    path('contact/', views.contact, name='contact'),
    path("courses/", views.courses, name="courses"),
    path('courses/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('uploadImage/', views.uploadImage, name='uploadImage'),
    path('contactUpload/', views.contactUpload, name='contactUpload'),
    path("student_list/", views.student_list, name="student_list"),
    path('student_list/student_details/<int:id>', views.student_details, name='student_details'),
    path('studentInfo/', views.studentInfo, name='studentInfo'),
    path('studentInfoUpload/', views.studentInfoUpload, name='studentInfoUpload'),
    path('studentProfile/', views.studentProfile, name='studentProfile'),
    path('pdf/', views.getPdf, name='pdf'),
    path('generate_pdf_file/', views.generate_pdf_file, name='generate_pdf_file'),
    path('circular/', views.circular, name='circular'),
    path('signup', views.signup, name='signup'),
    # path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('log_out', views.log_out, name='log_out'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]
