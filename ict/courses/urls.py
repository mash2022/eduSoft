from django.urls import path 
from . import views

urlpatterns = [
    path("courses/", views.courses, name="b"),
    path('courses/details/<int:id>', views.details, name='details'),
]
