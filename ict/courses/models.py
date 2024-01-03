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
    total_cost=models.FloatField(null=True)
    description=models.TextField(max_length=255, null=True)
    teacher_image=models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='trainer_image')
    teacher_name=models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='trainer_name')

    def __str__(self):
        return f"{self.course_name} {self.total_cost}"
    
    def image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.course_image))
    
    def image_tag_2(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.trainer_image))

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
    course_name = models.ForeignKey(to=Course,related_name="course_notice",on_delete=models.SET_NULL,blank=True,null=True,)
    admission_open=models.DateTimeField()
    admission_close=models.DateTimeField()

class CustomSettings(models.Model):
    logo=models.ImageField(upload_to='logo')
    institute_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
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
    course_name = models.ForeignKey(to=Course,related_name="courses",on_delete=models.SET_NULL,blank=True,null=True,)
    address=models.TextField()
    payment_agent=models.ForeignKey(to=PaymentAgent,related_name="payment_agents",on_delete=models.SET_NULL,blank=True,null=True,)
    taxInId=models.CharField(max_length=30, null=True)
    date=models.DateField(auto_now=True, null=True)
    is_active=models.BooleanField(default=False)
    is_approved=models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name}|{self.father_name}'

class PaymentAdmission(models.Model):
    paymentAgent=models.CharField(max_length=15)
    taxInId=models.CharField(max_length=30)
    date=models.DateField(auto_now=True)
    name=models.ForeignKey(StudentInfo, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}|{self.paymentAgent}|{self.taxInId}|{self.date}'
    class Meta:
        ordering=['name']

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
    student_info=models.OneToOneField(StudentInfo, on_delete=models.CASCADE, null=True)
    payment_amount=models.FloatField()
    total_cost=models.ForeignKey(Course, related_name='cost', on_delete=models.CASCADE)
    due_amount=models.FloatField()
    payment_date=models.DateField()

    def __str__(self):
        return f'{self.student_info}'