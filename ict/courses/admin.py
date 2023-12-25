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
    list_display=['course_name','admission_open', 'admission_close']
admin.site.register(Admission, AdmissionAdmin)

class AdmissionFormAdmin(admin.ModelAdmin):
    list_display=['student_name_ban', 'student_name_eng', 'father_or_hus_name_ban', 'father_or_hus_name_eng', 'village_ban', 'village_eng', 'post_office_ban', 'post_office_eng', 'upozila_ban', 'upozila_eng', 'district_ban', 'district_eng', 'religion', 'nid', 'mobile', 'nationality', 'blood_group', 'marrietal_status', 'age', 'edu_qualification', 'is_pharmacy_have', 'pharmacy_name_address', 'past_training_name', 'student_image', 'admission_date']
admin.site.register(AdmissionForm, AdmissionFormAdmin)

class CustomSettingsAdmin(admin.ModelAdmin):
    list_display=['image_tag','logo', 'institute_name', 'address']
admin.site.register(CustomSettings, CustomSettingsAdmin)

class StudentInfoAdmin(admin.ModelAdmin):
    list_display=['name', 'fatherName', 'mobile', 'email', 'courseName', 'address']
admin.site.register(StudentInfo, StudentInfoAdmin)

class PaymentAdmissionAdmin(admin.ModelAdmin):
    list_display=['studentInfo', 'paymentAgent', 'taxInId', 'date']
admin.site.register(PaymentAdmission, PaymentAdmissionAdmin)

class MyVideoAdmin(admin.ModelAdmin):
    list_display = ["title","video","details"]
admin.site.register(MyVideo, MyVideoAdmin)