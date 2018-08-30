from .models import Application
from django import forms

UNIVERSITY_LIST = ("UTS","UNSW","USYD","UWS","UOW", "UON","TAFE", "MQU")
UNIVERSITY_CHOICES= []
for r in UNIVERSITY_LIST:
			UNIVERSITY_CHOICES.append((r,r))

class ApplicationForm(forms.Form):
	class Meta:
		model = Application
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
	slides = forms.FileField(
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

#	<form id="startupcup-application" enctype="multipart/form-data"action="{% url 'application' %}" method="post">
#		<div class="form-group">
#				<label for="InputEmail">Email address</label>
#				<input type="email" class="form-control" id="InputEmail" aria-describedby="emailHelp" placeholder="Enter email">
#			</div>
#			<div class="form-group">
#				<label for="InputPassword">Password</label>
#				<input type="password" class="form-control" id="InputPassword" placeholder="Password">
#			</div>
#			<label for="FormControlFile"> file input</label>
#			<input type="file" class="form-control-file" id="FormControlFile">
#			<button type="submit" class="btn btn-primary">Submit</button>
#		</form>
