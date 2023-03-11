from django.urls import path 
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path("courses/", views.courses, name="courses"),
    path("courses2/", views.courses2, name="courses2"),
    path('courses/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
