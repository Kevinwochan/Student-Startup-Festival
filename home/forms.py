from django import forms

UNIVERSITY_LIST = ("UTS","UNSW","USYD","UWS","UOW", "UON","TAFE", "MQU")
UNIVERSITY_CHOICES= []
for r in UNIVERSITY_LIST:
            UNIVERSITY_CHOICES.append((r,r))

class applicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    university = forms.ChoiceField(choices=UNIVERSITY_CHOICES);
    pdf = forms.FileField()
    comments = forms.CharField(widget=forms.Textarea)
