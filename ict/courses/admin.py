from django.contrib import admin
from .models import Course

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display=('course_name', 'course_duration', 'course_code')
admin.site.register(Course, CourseAdmin)
