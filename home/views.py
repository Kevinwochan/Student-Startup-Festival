from .gmail import *
from django.core.mail import EmailMessage
from django import forms
from django.shortcuts import render
from .forms import applicationForm
from django.core.files.uploadedfile import SimpleUploadedFile

def homepage (request):
        return render(request,'landing.html')

def startupcup (request):
        return render(request,'startupcup.html')

def sponsors (request):
        return render(request,'sponsors.html')

def festival (request):
        return render(request,'festival.html')

def application (request):
    if request.method == 'POST':
        application = applicationForm(request.POST, request.FILES)
        if application.is_valid():
            name = application.cleaned_data['name']
            email_address = application.cleaned_data['email']
            pdf = application.cleaned_data['pdf']
            message = name + "\n" + email_address + "\n" + application.cleaned_data['comments']
            recipients = ('Operations@textbook.ventures',
                        'Kevinwochan@gmail.com',
                        'Clinton@textbook.ventures')
            '''
            email = CreateMessageWithAttachment(
                                 'Operations@textbook.ventures',
                                 recipients,
                                 'SSF Application: '+ name, 
                                 message,
                                 pdf.file.getvalue(),
                                 pdf.name
            )
            email.send()
            '''
            email = EmailMessage(
                                 'SSF Application: '+ name, 
                                 message,
                                 'Operations@textbook.ventures',
                                 recipients
            )
            email.attach (pdf.name,
                          pdf.file.getvalue(),
                          mimetypes.guess_type(pdf.name)[0]
            )
            email.send(fail_silently=False)
            return render(request,'application.html', {'application':application})
        else:
            return render(request,'application.html', {'application':application})

    else:
        application = applicationForm()
        return render(request,'application.html', {'application':application})


