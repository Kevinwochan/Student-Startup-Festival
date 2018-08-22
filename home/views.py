from django.core.mail import EmailMessage
from django import forms
from django.shortcuts import render
from .forms import applicationForm

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
        application = applicationForm(request.POST)
        if application.is_valid():
            name = form.cleaned_data['email']
            email_address = form.cleaned_data['email']
            message = name + "\n" + email + "\n" + form.cleaned_data['comments']
            recipients = ('operations@textbook.ventures',
                        'kevinwochan@gmail.com',
                        'Clinton@textbook.ventures')
            email = EmailMessage('SSF Application: '+name, message,
                                'operations@textbook.ventures',
                                recipients,
                                )
            email.attach_file(pdf)
            email.send(fail_silently=False)
            return render(request,'application.html', {'application':application})
        else:
            return render(request,'application.html', {'application':application})

    else:
        application = applicationForm()
        return render(request,'application.html', {'application':application})
