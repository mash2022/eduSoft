from django import forms
from .models import *
from django.forms import DateField, TextInput, EmailInput, Textarea

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['title', 'photo', 'details']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name', 'email', 'subject', 'message']
        widgets={
            'name':TextInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Your name'            
            }),
            'email':EmailInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'Your email'            
            }),
            'subject':TextInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'Subject'
            }),
            'message':Textarea(attrs={
            'class':'form-control',
            'style':'row:5;',
            'placeholder':'Message'
            })
        }

class Admission_form(forms.ModelForm):
    class Meta:
        model=AdmissionForm
        fields=['student_name','father_name','edu_qualification']
        widgets={
            'student_name':TextInput(attrs={
                'class':'form-control required',
                'style':'max_width: 50px;',
                'placeholder':'Name of student'
            }),
            'father_name':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'Name of father'
            }),
            'edu_qualification':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'Educational qualification'
            })
        }

class RmpLmfForm(forms.ModelForm):
    class Meta:
        model=RmpLmf
        fields=['student_name_ban', 'student_name_eng', 'father_or_hus_name_ban', 'father_or_hus_name_eng', 'village_ban', 'village_eng', 'post_office_ban', 'post_office_eng', 'upozila_ban', 'upozila_eng', 'district_ban', 'district_eng', 'religion', 'nid', 'mobile', 'nationality', 'blood_group', 'marrietal_status', 'age', 'edu_qualification', 'is_pharmacy_have', 'pharmacy_name_address', 'past_training_name']  
        widgets={
            'student_name_ban':TextInput(attrs={
                'class':'form-control required',
                'style':'max_width: 50px;',
                'placeholder':'Student name in Bangla'}),
        }      