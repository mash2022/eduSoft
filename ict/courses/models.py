from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=255)
    course_duration=models.CharField(max_length=255)
    course_code=models.IntegerField(null=True)
    course_credit=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.course_name} {self.course_duration}"


