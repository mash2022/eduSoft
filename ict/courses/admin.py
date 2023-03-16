from django.contrib import admin
from .models import Course
from .models import Teacher

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_name', 'course_duration', 'course_code')
admin.site.register(Course, CourseAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display=('teacher_name', 'teacher_details', 'teacher_image')
admin.site.register(Teacher,TeacherAdmin)

