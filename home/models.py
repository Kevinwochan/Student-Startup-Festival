from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
UNIVERSITY_LIST = ("UTS","UNSW","USYD","UWS","UOW", "UON","TAFE", "MQU")
UNIVERSITY_CHOICES= []
for r in UNIVERSITY_LIST:
    UNIVERSITY_CHOICES.append((r,r))

class Application(models.Model):

    name = models.CharField( max_length=100, default='') 

    email = models.EmailField( max_length=100, default='')

    university = models.CharField( max_length=100, choices=UNIVERSITY_CHOICES,default='')

    summary = models.FileField(default='', upload_to='applications/')

    pitch_deck = models.FileField(default='', upload_to='applications/')

    comments = models.CharField(max_length=500, default='')

class ApplicationForm(ModelForm):
    name = forms.CharField(
            max_length=100,
            label="Name",
            widget = forms.TextInput(attrs={'class':"form-control",
                        'placeholder':"John Smith"
            }),
            required=True
    )

    email = forms.EmailField(
            max_length=100,
            label="Email",
            widget = forms.EmailInput(attrs={'class':"form-control",
                        'placeholder':"example@email.com"
            }),
            required=True

    )
    university = forms.ChoiceField(
            choices=UNIVERSITY_CHOICES,
            label = "University",
            widget = forms.Select(attrs={'class':"form-control",
                        'placeholder':"select one"
            }),
            required=True
    )
    summary = forms.FileField(
            label="One-Page Summary",
            widget = forms.FileInput(attrs={'class':"form-control-file",
                        'placeholder':"pdf format only"
            }),
            required=True
    )
    pitch_deck = forms.FileField(
            label="Pitch Deck",
            widget = forms.FileInput(attrs={'class':"form-control-file",
                        'placeholder':"pdf format only"
            }),
            required=True
    )    
    comments = forms.CharField(
            label="Additional comments",
            widget = forms.Textarea(attrs={'class':"form-control"}),
            required=False
    )


    class Meta:
        model = Application
        fields = ['name','email','university','summary','pitch_deck','comments']
        """
        widgets = {
                'name': Textinput(attrs={'class':"form-control",
                        'placeholder':"John Smith"
                }),
                'email': EmailInput(attrs={'class':"form-control",
                        'placeholder':"example@email.com"
                }),
                'university' : Select(attrs={'class':"form-control",
                        'placeholder':"select one"
                }),
                'summary': FileInput(attrs={'class':"form-control-file",
                        'placeholder':"pdf format only"
                }),
                'pitch_deck': FileInput(attrs={'class':"form-control-file",
                            'placeholder':"pdf format only"
                }),
                'comments' : Textarea(attrs={'class':"form-control"
                })
        }
        """
