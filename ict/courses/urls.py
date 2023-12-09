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
]
