from django import forms
from .models import User


class UserForm(forms.ModelForm):
	first_name      = forms.CharField(max_length=250, required=True)
	last_name       = forms.CharField(max_length=250, required=True)
	date_of_birth   = forms.DateField(required=False)
	gender          = forms.CharField(max_length=250, required=False)
	citizenship     = forms.CharField(max_length=250, required=False)
	contact_cell    = forms.CharField(max_length=250, required=False)
	bio             = forms.CharField(max_length=250, required=False)
	job_title       = forms.CharField(max_length=250, required=False)
	home_address    = forms.CharField(max_length=250, required=False)

	class Meta:
		model = User
		fields = ('first_name','last_name','date_of_birth','gender','citizenship','contact_cell','bio','job_title','home_address')