from django.shortcuts import render

def homepage (request):
        return render(request,'landing.html')

def startupcup (request):
        return render(request,'startupcup.html')

def sponsors (request):
        return render(request,'sponsors.html')

def festival (request):
        return render(request,'festival.html')
