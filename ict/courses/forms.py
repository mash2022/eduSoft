from django import forms
from .models import *
from django.forms import NumberInput, TextInput,EmailInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
        fields=['name', 'father_name', 'mobile_number', 'email','village','post_office','upozilla','district','nid','date_of_birth','student_pic','edu_qualification','edu_cirtificate','pharmacy','pharmacy_address', 'course_name','total_cost', 'payment_amount', 'payment_agent','taxInId',]
        agent_name = forms.ModelMultipleChoiceField(queryset=PaymentAgent.objects.all(), widget=forms.CheckboxSelectMultiple)
        course_name = forms.ModelChoiceField(to_field_name='course_name', queryset=Course.objects.all())
        student_pic=forms.ImageField()
        edu_cirtificate=forms.ImageField()
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
            'mobile_number':NumberInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Mobile number'            
            }),
            'email':EmailInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'email'            
            }),
            'village':TextInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'permanent'            
            }),
            'post_office':TextInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'permanent'            
            }),
            'upozilla':TextInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'permanent'            
            }),
            'district':TextInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'permanent'            
            }),
            'pharmacy_address':TextInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Pharmacy name and address'            
            }),
            'nid':NumberInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'National id'            
            }),
            'edu_qualification':TextInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Educational Qualification example: SSC'            
            }),
            'payment_amount':NumberInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Educational Qualification example: SSC'            
            }),
        }

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    membership_number=models.CharField(max_length=55)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user