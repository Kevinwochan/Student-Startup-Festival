from django.conf import settings
from django import forms
from django.shortcuts import render
from .models import Application
from .models import ApplicationForm
from .gmail import *

def homepage (request):
        return render(request,'landing.html', {'page':'homepage'})

def subscribed (request):
        return render(request,'subscribed.html', {'page':'subscribed'})


def startupcup (request):
    return render(request, 'startupcup.html', {'page':'startupcup'})

def sponsors (request):
    return render(request, 'sponsors.html', {'page':'sponsors'})

def application (request):
    if request.method == 'POST':
        applicationForm = ApplicationForm(request.POST, request.FILES)
        if applicationForm.is_valid():
            name = applicationForm.cleaned_data['name']
            email_address = applicationForm.cleaned_data['email']
            summary = applicationForm.cleaned_data['summary']
            slides = applicationForm.cleaned_data['slides']
            
            newApplication = applicationForm.save()
            send_submission_email(newApplication)
            return render(request, 'success.html')
        else:
            return render(request,'application.html', 
                    {'page':'application', 'application':application})

    else:
        application = ApplicationForm()
        return render(request,'application.html', 
                {'page':'applicaton', 'application':application})

def send_submission_email(application):

        message = "Name: " + application.name + "\n" 
        message += "Email Address: " + application.email + "\n" 
        message += "Submmary: " + application.summary.url
        message += "Slides: " + application.slides.url
        message += "Additional Comments\n" + application.comments
        recipients = ['Operations@textbook.ventures',
                       'Kevinwochan@gmail.com'
        ]
        email = create_message(recipients, 'SSF Application: '+ application.name, message)
        print(message)
        send_message(email)
        return
