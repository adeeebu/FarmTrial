from django.shortcuts import render
from .forms import FarmerProfileForm

# Create your views here.
def join(request):
	print() 
	if request.method == 'POST': 
		form = FarmerProfileForm(request.POST or None)

		if form.is_valid():
			form.save()
			return render(request, 'ProfileSaved.html')

	else: 
		return render(request, 'profiles.html')



		

 	
 

