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
