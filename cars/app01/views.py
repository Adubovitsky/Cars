from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Vehicles
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def main_view(request):
	cars = Vehicles.objects.all()
	return render(request, 'app01/index.html', context = {'cars': cars})

def contacts(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			message = form.cleaned_data['message']
			email = form.cleaned_data['email']
			send_mail('', message, 'from@example.com', [email], fail_silently=True, )
			return HttpResponseRedirect(reverse('cars:index') )
		else:
			return render(request, 'app01/contact.html', context={'form': form})
	else:
		form = ContactForm
	return render(request, 'app01/contact.html', context={'form':form})

def search(request):
	return render(request, 'app01/search.html')