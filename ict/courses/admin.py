from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_name', 'image_tag', 'course_duration', 'course_code', 'course_image')
admin.site.register(Course, CourseAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display=['teacher_name', 'image_tag', 'teacher_details', 'teacher_image']
admin.site.register(Teacher,TeacherAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]
admin.site.register(Event, EventAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ["title","image_tag","photo","details"]
admin.site.register(Image, ImageAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display=['title', 'description', 'aboutImage', 'image_tag']
admin.site.register(About, AboutAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'subject', 'message']
admin.site.register(Contact, ContactAdmin)

class NoticeAdmin(admin.ModelAdmin):
    list_display=['notice_title', 'notice_details','image_tag','notice_image']
admin.site.register(Notice, NoticeAdmin)

class AdmissionAdmin(admin.ModelAdmin):
    list_display=['course_name','admission_open', 'admission_close','admission_link']
admin.site.register(Admission, AdmissionAdmin)