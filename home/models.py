from django.db import models
from django.forms import ModelForm
from django import forms

class Application(models.Model):

    name = models.CharField( max_length=100, default='') 

    email = models.EmailField( max_length=100, default='')

    institution = models.CharField( max_length=100, default='') 

    identification = models.ImageField(default='', upload_to='applications/')

    summary = models.FileField(default='', upload_to='applications/')

    slides = models.FileField(default='', upload_to='applications/')

    comments = models.CharField(max_length=500, default='')

class ApplicationForm(ModelForm):
    name = forms.CharField(
            max_length=100,
            label='Name',
            widget = forms.TextInput(attrs={'class':'form-control',
                        'placeholder':'John Smith'
            }),
            required=True
    )

    email = forms.EmailField(
            max_length=100,
            label='Email',
            widget = forms.EmailInput(attrs={'class':'form-control',
                        'placeholder':'example@email.com'
            }),
            required=True

    ) 
    institution = forms.CharField(
            max_length=100,
            label='Tertiary Institution Name',
            widget = forms.TextInput(attrs={'class':'form-control',
                        'placeholder':''
            }),
            required=True
    )
    identification = forms.ImageField(
            label='Photo of valid student identification',
            widget = forms.ClearableFileInput(attrs={'class':'form-control-file',
                        'placeholder':''
            }),
            required=True
    )
    summary = forms.FileField(
            label='One-Page Summary',
            widget = forms.ClearableFileInput(attrs={'class':'form-control-file',
                        'placeholder':'pdf format only'
            }),
            required=True
    )
    slides = forms.FileField(
            label='Pitch Deck',
            widget = forms.ClearableFileInput(attrs={'class':'form-control-file',
                        'placeholder':'pdf format only'
            }),
            required=True
    )    
    comments = forms.CharField(
            label='Additional comments',
            widget = forms.Textarea(attrs={'class':'form-control'}),
            required=False
    )
    class Meta:
        model = Application
        fields = ['name','email','institution','identification','summary','slides','comments']
