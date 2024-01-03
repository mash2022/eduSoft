from django import forms
from .models import *
from django.forms import ModelForm, DateField, TextInput,EmailInput, Textarea

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


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model=StudentInfo
        fields=['name', 'father_name', 'mobile_number', 'email', 'course_name', 'address','payment_agent','taxInId']
        agent_name = forms.ModelMultipleChoiceField(queryset=PaymentAgent.objects.all(), widget=forms.CheckboxSelectMultiple)
        coursName=forms.CharField()
        widgets={
            'name':TextInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Your name'            
            }),
            'father_name':TextInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Father name'            
            }),
            'mobile':TextInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Mobile number'            
            }),
            'email':EmailInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'email'            
            }),
            # 'course_name':TextInput(attrs={
            # 'class':'form-control required',
            # 'style':'max_width:50px;',
            # 'placeholder':''            
            # }),
            'address':Textarea(attrs={
            'class':'form-control',
            'style':'row:5;',
            'placeholder':'Message'
            }),
            'taxInId':TextInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'TaxInId'            
            }),
        }

class PaymentAdmissionForm(forms.ModelForm):
    class Meta:
        model=PaymentAdmission
        fields=['paymentAgent','taxInId']
        widgets={
            'paymentAgent':TextInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'Your email'            
            }),
            'taxInId':TextInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'Subject'
            }),
        }

