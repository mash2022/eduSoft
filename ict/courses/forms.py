from django import forms
from .models import *
from django.forms import DateInput, FileInput, ModelForm, DateField, NumberInput, Select, SelectMultiple, TextInput,EmailInput, Textarea, DateInput
from django.contrib.auth.forms import UserCreationForm

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

# class SignupForm(UserCreationForm):
#     username=models.CharField(max_length=55)
#     mobile_number=models.IntegerField()
#     email=models.EmailField()
#     membership_number=models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
#     password=models.CharField(max_length=30)
#     class Meta:
#         model = Signup
#         fields = ['username', 'mobile_number', 'email', 'membership_number', 'password']

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     phone_no = forms.CharField(max_length = 20)
#     first_name = forms.CharField(max_length = 20)
#     last_name = forms.CharField(max_length = 20)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'phone_no', 'password1', 'password2']

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model=Login
#         fields=['membership_number', 'password']
