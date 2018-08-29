from django.conf import settings
from django import forms
from django.shortcuts import render
from .models import Application
from .models import ApplicationForm
from .gmail import *

def homepage (request):
        return render(request,'landing.html', {'page':'homepage'})

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
            summary.name += email_address
            pitch_deck = applicationForm.cleaned_data['pitch_deck']
            pitch_deck.name += email_address
            """
            message = "Name: " + name + "\n" 
            message += "Email Address: " + email_address + "\n" 
            message += "Additional Comments\n" + application.cleaned_data['comments']

            recipients = ['Operations@textbook.ventures',
                           'Kevinwochan@gmail.com'
            ]

            attachments = [summary,pitch_deck]

            email = create_message_with_attachment(
                                 recipients,
                                 'SSF Application: '+ name, 
                                 message,
                                 attachments
            )
            send_confirmation_email(email_address)
            """
            #application = Application(name,email_address,summary,pitch_deck)
            applicationForm.save()
            return render(request, 'success.html')
        else:
            return render(request,'application.html', 
                    {'page':'application', 'application':application})

    else:
        application = ApplicationForm()
        return render(request,'application.html', 
                {'page':'applicaton', 'application':application})

def save_file(file):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


