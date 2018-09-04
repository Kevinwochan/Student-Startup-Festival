from django.conf import settings
from django import forms
from django.shortcuts import render
from .models import Application
from .models import ApplicationForm
from .gmail import *

def handler403(request, exception, template_name='403.html'):
        return render(request,'403.html', {'page':'403'})

def handler404(request, exception, template_name='404.html'):
        return render(request,'404.html', {'page':'404'})

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
        message += "University: " + application.university + "\n" 
        message += "ID: https://ssf.textbook.ventures" + application.identification.url+ "\n"
        message += "Summary: https://ssf.textbook.ventures" + application.summary.url+ "\n"
        message += "Slides: https://ssf.textbook.ventures" + application.slides.url+ "\n"
        message += "Additional Comments\n" + application.comments
        recipients = ['Operations@textbook.ventures',
                       'Kevinwochan@gmail.com',
                       'Jenny@textbook.ventures',
                       'Clinton@textbook.ventures',
        ]
        email = create_message(recipients, 'SSF Application: '+ application.name, message)
        print(message)
        send_message(email)
        return
