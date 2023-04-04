from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path("courses/", views.courses, name="courses"),
    path("teachers/", views.teachers, name="teachers"),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('image/', views.image, name='image'),
    path('admission/', views.admission, name='admission'),
    path('contact/', views.contact, name='contact'),
    path("courses2/", views.courses2, name="courses2"),
    path('courses/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('uploadImage/', views.uploadImage, name='uploadImage'),
]
