from django.conf import settings
from django import forms
from django.shortcuts import render
from .forms import applicationForm
from .gmail import *

def homepage (request):
        return render(request,'landing.html', {'page':'homepage'})

def startupcup (request):
    return render(request, 'startupcup.html', {'page':'startupcup'})

def sponsors (request):
    return render(request, 'sponsors.html', {'page':'sponsors'})

def application (request):
    if request.method == 'POST':
        application = applicationForm(request.POST, request.FILES)

        if application.is_valid():
            name = application.cleaned_data['name']
            email_address = application.cleaned_data['email']
            summary = application.cleaned_data['summary']
            pitch_deck = application.cleaned_data['pitch_deck']

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
            service = initialise_gmail() 
            send_message (email)
            '''
            subject = 'SSF Application: '+ name, 
            email = EmailMessage(
                                subject,
                                message,
                                settings.EMAIL_HOST_USER,
                                recipients
            )
            email.attach (pdf.name,
                          pdf.file.getvalue(),
                          mimetypes.guess_type(pdf.name)[0]
            )
            email.send(fail_silently=False)
            '''
            send_confirmation_email(email_address)
            return render(request, 'success.html')
        else:
            return render(request,'application.html', 
                    {'page':'application', 'application':application})

    else:
        application = applicationForm()
        return render(request,'application.html', 
                {'page':'applicaton', 'application':application})


