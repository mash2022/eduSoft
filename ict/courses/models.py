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
    admission_link=models.URLField((""), max_length=200)

