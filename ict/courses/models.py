from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=255)
    course_duration=models.CharField(max_length=255)
    course_code=models.IntegerField(null=True)
    course_credit=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.course_name} {self.course_duration}"

class Teacher(models.Model):
    teacher_name=models.CharField(max_length=255)
    teacher_details=models.TextField()
    teacher_image=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.teacher_name
    
class Event(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')

class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')
    

    

