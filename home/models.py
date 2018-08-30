from django.db import models
from django.forms import ModelForm
from django import forms

UNIVERSITY_CHOICES = [
        ('UTS', 'University of Technology Sydney'),
        ('UNSW', 'University of New South Wales'), 
        ('USYD', 'University of Sydney'),
        ('MQU', 'University of Macquarie'),
        ('UOW', 'University of Wollongong'),
        ('ACU', 'Australian Catholic University'),
        ('UNE', 'University of New England'),
        ('SCU', 'Southern Cross University'),
        ('CSU', 'Charles Sturt University'),
        ('TAFE','TAFE')
]

class Application(models.Model):

    name = models.CharField( max_length=100, default='') 

    email = models.EmailField( max_length=100, default='')

    university = models.CharField( max_length=100, choices=UNIVERSITY_CHOICES,default='')

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
    university = forms.ChoiceField( choices=UNIVERSITY_CHOICES,
            label = 'University',
            widget = forms.Select(attrs={'class':'form-control',
                        'placeholder':'select one'
            }),
            required=True
    )
    summary = forms.FileField(
            label='One-Page Summary',
            widget = forms.FileInput(attrs={'class':'form-control-file',
                        'placeholder':'pdf format only'
            }),
            required=True
    )
    slides = forms.FileField(
            label='Pitch Deck',
            widget = forms.FileInput(attrs={'class':'form-control-file',
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
        fields = ['name','email','university','summary','slides','comments']
