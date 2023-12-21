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

class Admission_form(forms.ModelForm):
    class Meta:
        model=AdmissionForm
        fields='__all__'
        #fields=['student_name_ban', 'student_name_eng', 'father_or_hus_name_ban', 'father_or_hus_name_eng', 'village_ban', 'village_eng', 'post_office_ban', 'post_office_eng', 'upozila_ban', 'upozila_eng', 'district_ban', 'district_eng', 'religion', 'nid', 'mobile', 'nationality', 'blood_group', 'marrietal_status', 'age', 'edu_qualification', 'is_pharmacy_have', 'pharmacy_name_address', 'past_training_name','student_image']  
        widgets={
            'student_name_ban':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 300px;',
                'placeholder':'নাম (বাংলায়)'}),
            'student_name_eng':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 300px;',
                'placeholder':'Name (English)'}),
            'father_or_hus_name_ban':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'পিতা/স্বামীর নাম'}),
            'father_or_hus_name_eng':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'Father/Husband name'}),
            'village_ban':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'গ্রাম'}),
            'village_eng':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'Village'}),
            'post_office_ban':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'ডাকঘর'}),
            'post_office_eng':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'Post office'}),
            'upozila_ban':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'উপজেলা'}),
            'upozila_eng':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'Upozilla'}),
            'district_ban':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'জেলা'}),
            'district_eng':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'District'}),
            'nid':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'NID'}),
            'mobile':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'Mobile number'}),
            'nationality':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'Nationality'}),
            'blood_group':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'Blood group'}),
            'age':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'Age'}),
            'pharmacy_name_address':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',
                'placeholder':'If yes, Pharmacy name and address'}),
            'past_training_name':TextInput(attrs={
                'class':'form-control',
                'style':'max_width: 50px;',}),               
        } 

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model=StudentInfo
        fields=['name', 'fatherName', 'mobile', 'email', 'courseName', 'address']
        widgets={
            'name':TextInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Your name'            
            }),
            'fatherName':TextInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Your name'            
            }),
            'mobile':TextInput(attrs={
            'class':'form-control required',
            'style':'max_width:50px;',
            'placeholder':'Your name'            
            }),
            'email':EmailInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'Your email'            
            }),
            'courseName':TextInput(attrs={
            'class':'form-control',
            'style':'max_width:300px;',
            'placeholder':'Subject'
            }),
            'address':Textarea(attrs={
            'class':'form-control',
            'style':'row:5;',
            'placeholder':'Message'
            })
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

