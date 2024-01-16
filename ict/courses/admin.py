from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_name', 'image_tag', 'course_duration', 'course_code', 'course_image','description', 'teacher_image', 'teacher_name')
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
    list_display=['name', 'father_name', 'mobile_number', 'email','village','post_office','upozilla','district','nid','date_of_birth','student_image_tag','edu_qualification','cirtificate_image_tag','pharmacy','pharmacy_address','course_name','payment_amount', 'payment_agent', 'taxInId', 'admission_date', 'is_active', 'is_approved', 'membership_number']
    search_fields=['name', 'mobile_number']
admin.site.register(StudentInfo, StudentInfoAdmin)

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
    list_display=['student_info', 'payment_date', 'total_cost', 'payment_amount', 'due']
    search_fields=['student_info__name','student_info__mobile_number']
admin.site.register(Payment, PaymentAdmin)

class CommitteeAdmin(admin.ModelAdmin):
    list_display=['member_name', 'member_details', 'image_tag','member_voice']
admin.site.register(Committee, CommitteeAdmin)

class CostAdmin(admin.ModelAdmin):
    list_display=['course_name', 'total_cost']
admin.site.register(Cost, CostAdmin)

class Custom_UserAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'email', 'user_type']
admin.site.register(Custom_User, Custom_UserAdmin) 