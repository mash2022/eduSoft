from django.contrib import admin
from .models import Course, Teacher, Event, Image

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_name', 'course_duration', 'course_code')
admin.site.register(Course, CourseAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display=['teacher_name', 'teacher_details', 'teacher_image']
admin.site.register(Teacher,TeacherAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]
admin.site.register(Event, EventAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Image, ImageAdmin)

