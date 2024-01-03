from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_name', 'image_tag', 'course_duration', 'course_code', 'course_image', 'total_cost', 'description', 'teacher_image', 'teacher_name')
admin.site.register(Course, CourseAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display=['teacher_name', 'image_tag', 'teacher_details']
admin.site.register(Teacher,TeacherAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", 'event_date', 'description']
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

class AdmissionNoticeAdmin(admin.ModelAdmin):
    list_display=['course_name','admission_open', 'admission_close']
admin.site.register(AdmissionNotice, AdmissionNoticeAdmin)

class CustomSettingsAdmin(admin.ModelAdmin):
    list_display=['image_tag','logo', 'institute_name', 'address', 'email']
admin.site.register(CustomSettings, CustomSettingsAdmin)

class StudentInfoAdmin(admin.ModelAdmin):
    list_display=['name', 'father_name', 'mobile_number', 'email', 'course_name', 'address', 'payment_agent', 'taxInId', 'date', 'is_active', 'is_approved']
    search_fields=['name', 'mobile']
admin.site.register(StudentInfo, StudentInfoAdmin)

class PaymentAdmissionAdmin(admin.ModelAdmin):
    model=PaymentAdmission
    list_display=['name', 'paymentAgent', 'taxInId', 'date']
admin.site.register(PaymentAdmission, PaymentAdmissionAdmin)

class MyVideoAdmin(admin.ModelAdmin):
    list_display = ["title","video","details"]
admin.site.register(MyVideo, MyVideoAdmin)

class CircularAdmin(admin.ModelAdmin):
    list_display = ["title","image_tag","circular","details"]
admin.site.register(Circular, CircularAdmin)

class PaymentAgentAdmin(admin.ModelAdmin):
    list_display=['agent_name', 'agent_number']
admin.site.register(PaymentAgent, PaymentAgentAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display=['student_info', 'payment_amount', 'total_cost','due_amount','payment_date']
admin.site.register(Payment, PaymentAdmin)