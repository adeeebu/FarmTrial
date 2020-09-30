from django import forms
from .models import FarmerProfile

class FarmerProfileForm(forms.ModelForm):
	class Meta:
		model = FarmerProfile
		fields = [ 'fname', 'lname', 'email', 'dist', 'state', 'passwd' ]

