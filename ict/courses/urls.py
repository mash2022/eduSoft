from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("courses/", views.courses, name="courses"),
    path('courses/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
