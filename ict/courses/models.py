from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image as Im


# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=255)
    course_duration=models.CharField(max_length=255)
    course_code=models.IntegerField(null=True)
    course_credit=models.IntegerField(null=True)
    course_image=models.ImageField(upload_to='pics')

    def __str__(self):
        return f"{self.course_name} {self.course_duration}"
    
    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.course_image))

class Notice(models.Model):
    notice_title=models.CharField(max_length=255)
    notice_details=models.TextField(max_length=255)
    notice_image=models.ImageField(upload_to='pics')

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.notice_image))

class Teacher(models.Model):
    teacher_name=models.CharField(max_length=255)
    teacher_details=models.TextField()
    teacher_image=models.ImageField(upload_to='pics')

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150"/>' %(self.teacher_image))

    def save(self):
        super().save()
        img=Im.open(self.teacher_image.path)
        if img.height>300 or img.width>300:
            output_size=(300, 300)
            img.thumbnail(output_size)
            img.save(self.teacher_image.path)
    
class Event(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')

class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    details= models.CharField(max_length=255)

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.photo))

    def save(self):
        super().save()
        img=Im.open(self.photo.path)
        if img.height>300 or img.width>150:
            output_size=(300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

class About(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    aboutImage=models.ImageField(upload_to='pics')

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150"/>' % (self.aboutImage))

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()

class Admission(models.Model):
    course_name=models.CharField(max_length=255)
    admission_open=models.DateTimeField()
    admission_close=models.DateTimeField()

class AdmissionForm(models.Model):
    edu_choice=(('SSC', 'SSC'), ('HSC', 'HSC'), ('HONOURS', 'HONOURS'), ('MASTERS', 'MASTERS'))
    religion=(('ISLAM', 'ISLAM'), ('OTHERS', 'OTHERS'))
    pharmacy=(('YES', 'YES'), ('NO', 'NO'))
    marrietal_status=(('MARRIED', 'MARRIED'), ('UNMARRIED', 'UNMARRIED'))

    student_name_ban=models.CharField('Student name:', max_length=70)
    student_name_eng=models.CharField('', max_length=70)
    father_or_hus_name_ban=models.CharField('Father/Husband name:',max_length=70)
    father_or_hus_name_eng=models.CharField('', max_length=70)
    village_ban=models.CharField('Village:',max_length=50)
    village_eng=models.CharField('', max_length=50)
    post_office_ban=models.CharField('Post office:', max_length=50)
    post_office_eng=models.CharField('', max_length=50)
    upozila_ban=models.CharField('Upazilla:', max_length=50)
    upozila_eng=models.CharField('', max_length=50)
    district_ban=models.CharField('District:', max_length=50)
    district_eng=models.CharField('', max_length=50)
    religion=models.CharField('Religion:', max_length=10, choices=religion, default='ISLAM')
    nid=models.CharField('National ID no.:', max_length=30)
    mobile=models.CharField('Mobile number:', max_length=20)
    nationality=models.CharField('Nationality:', max_length=50)
    blood_group=models.CharField('Blood group:', max_length=20)
    marrietal_status=models.CharField('Marrital status:', max_length=50, choices=marrietal_status)
    age=models.CharField('Age:', max_length=50)
    edu_qualification=models.CharField('Educational qualification:', max_length=10, choices=edu_choice)
    is_pharmacy_have=models.CharField('Have any Pharmacy:', max_length=10, choices=pharmacy)
    pharmacy_name_address=models.CharField('Pharmacy name and address:', max_length=200)
    past_training_name=models.CharField('Have any training:', max_length=100)
    student_image=models.ImageField(upload_to='student_pic')
    admission_date=models.DateField(auto_now=True)

class CustomSettings(models.Model):
    logo=models.ImageField(upload_to='logo')
    institute_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    mobile_number=models.CharField(max_length=50)

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150"/>' % (self.logo))

class StudentInfo(models.Model):
    name=models.CharField(max_length=50)
    fatherName=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    email=models.EmailField()
    courseName=models.CharField(max_length=255)
    address=models.TextField()

class PaymentAdmission(models.Model):
    studentInfo=models.ForeignKey(StudentInfo, blank=False, null=True, on_delete=models.CASCADE)
    paymentAgent=models.CharField(max_length=15)
    taxInId=models.CharField(max_length=30)
    date=models.DateField(auto_now=True)

class MyVideo(models.Model):
    title = models.CharField(max_length=20)
    video = models.FileField(upload_to='videos/', null=True, verbose_name='')
    details= models.CharField(max_length=255)

    def __str__(self):
        return self.title + ": " + str(self.video)
    
    # def video_tag(self):
    #     return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.video))

    # def save(self):
    #     super().save()
    #     img=Im.open(self.photo.path)
    #     if img.height>300 or img.width>150:
    #         output_size=(300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.photo.path)   