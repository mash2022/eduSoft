from django.urls import path 
from . import views

urlpatterns = [
    path("courses/", views.courses, name="b"),
    path("a/", views.a, name="a"),
    path("c/", views.c, name="c"),
]
