from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image as Im

# Create your models here.
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=255)
    teacher_details=models.TextField()
    teacher_image=models.ImageField(upload_to='pics')

    def __str__(self):
        return f'{self.teacher_name}'

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150"/>' %(self.teacher_image))

    def save(self):
        super().save()
        img=Im.open(self.teacher_image.path)
        if img.height>300 or img.width>300:
            output_size=(300, 300)
            img.thumbnail(output_size)
            img.save(self.teacher_image.path)

class Course(models.Model):
    class Meta:
        verbose_name_plural='courses'
    course_name=models.CharField(max_length=255)
    course_duration=models.CharField(max_length=255)
    course_code=models.IntegerField(null=True)
    course_credit=models.IntegerField(null=True)
    course_image=models.ImageField(upload_to='pics')
    description=models.TextField(max_length=255, null=True)
    teacher_image=models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='trainer_image')
    teacher_name=models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='trainer_name')

    def __str__(self):
        return f"{self.course_name}"
    
    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.course_image))
    
    def image_tag_2(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.trainer_image))

class Cost(models.Model):
    course_name=models.ForeignKey(Course, on_delete=models.CASCADE)
    total_cost=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.total_cost}'

class Notice(models.Model):
    notice_title=models.CharField(max_length=255)
    notice_details=models.TextField(max_length=255)
    notice_image=models.ImageField(upload_to='pics')

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.notice_image))
    
class Event(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    event_date=models.DateField(null=True)
    description=models.TextField(max_length=255, null=True)

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
    description=models.TextField(max_length=4000)
    aboutImage=models.ImageField(upload_to='pics')

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150"/>' % (self.aboutImage))

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()

class AdmissionNotice(models.Model):
    # course_name=models.CharField(max_length=255)
    course_name = models.ForeignKey(to=Course,related_name="course_notice",on_delete=models.SET_NULL,blank=True,null=True)
    admission_open=models.DateTimeField()
    admission_close=models.DateTimeField()

class CustomSettings(models.Model):
    logo=models.ImageField(upload_to='logo')
    institute_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    regi_number=models.CharField(max_length=255, null=True)
    mono_regi_number=models.CharField(max_length=255, null=True)
    mobile_number=models.CharField(max_length=50)
    email=models.EmailField()

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150"/>' % (self.logo))

class PaymentAgent(models.Model):
    agent_name=models.CharField(max_length=40)
    agent_number=models.CharField(max_length=11)
    def __str__(self):
        return f'{self.agent_name} | {self.agent_number}'

class StudentInfo(models.Model):
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=50, unique=True, null=True)
    email=models.EmailField(unique=True, null=True)
    village=models.CharField(max_length=255, null=True)
    post_office=models.CharField(max_length=255, null=True)
    upozilla=models.CharField(max_length=255, null=True)
    district=models.CharField(max_length=255, null=True)
    nid=models.CharField(max_length=255, null=True)
    date_of_birth=models.DateField()
    student_pic=models.ImageField(upload_to='student_pic')
    edu_qualification=models.CharField(max_length=255, null=True)
    edu_cirtificate=models.ImageField(upload_to='cirtificate')
    pharmacy=models.BooleanField(null=True)
    pharmacy_address=models.CharField(max_length=255, null=True)
    course_name = models.ForeignKey(to=Course,related_name="courses",on_delete=models.SET_NULL,blank=True,null=True,)
    total_cost=models.ForeignKey(Cost, related_name='fee', on_delete=models.CASCADE, null=True)
    payment_amount=models.IntegerField(default=0, null=True)
    payment_agent=models.ForeignKey(to=PaymentAgent,related_name="payment_agents",on_delete=models.SET_NULL,blank=True,null=True)
    taxInId=models.CharField(max_length=30, null=True)
    admission_date=models.DateField(auto_now=True, null=True)
    is_active=models.BooleanField(default=False)
    is_approved=models.BooleanField(default=False)
    membership_number=models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f'{self.name}|{self.father_name}'

class MyVideo(models.Model):
    title = models.CharField(max_length=20)
    video = models.FileField(upload_to='videos/', null=True, verbose_name='')
    details= models.CharField(max_length=255)

    def __str__(self):
        return self.title + ": " + str(self.video)
    
class Circular(models.Model):
    title = models.CharField(max_length=20)
    circular = models.ImageField(upload_to='circulars')
    details= models.CharField(max_length=255)

    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.circular))

    def save(self):
        super().save()
        img=Im.open(self.circular.path)
        if img.height>300 or img.width>150:
            output_size=(300, 300)
            img.thumbnail(output_size)
            img.save(self.circular.path)

class Payment(models.Model):
    student_info=models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now=True)
    total_cost=models.ForeignKey(Cost, on_delete=models.CASCADE, null=True)
    payment_amount = models.IntegerField(default=0)

    # def __str__(self):
    #     return f'{self.student_info}'

    @property
    def due(self):
        if (self.payment_amount != None):
            due=self.total_cost - self.payment_amount
            return due

    
class Committee(models.Model):
    member_name=models.CharField(max_length=200)
    member_details=models.TextField()
    member_pic=models.ImageField(upload_to='committee_pics')
    member_voice=models.TextField(null=True)

    def __str__(self):
        return f'{self.member_name}'
    
    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150"/>' %(self.member_pic))

    def save(self):
        super().save()
        img=Im.open(self.member_pic.path)
        if img.height>300 or img.width>300:
            output_size=(300, 300)
            img.thumbnail(output_size)
            img.save(self.member_pic.path)

# class Sign_up(models.Model):
#     name=models.CharField(max_length=255)
#     mobile_number=models.IntegerField()
#     email=models.EmailField()
#     membership_number=models.CharField(max_length=255)
#     password=models.CharField(max_length=200)