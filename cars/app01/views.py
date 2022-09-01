from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.base import ContextMixin
from .models import Vehicles
from .forms import ContactForm, VehicleForm, SearchForm
from django.core.mail import send_mail
from django.core.management import commands, call_command
from app01.management.commands import filldb


# Create your views here.

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
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			Vehicles.objects.all().delete()
			brand = form.cleaned_data['car_brand']
			model = form.cleaned_data['car_model']
			call_command('filldb', brand, model)
			call_command('filldb_de', brand, model)
			return HttpResponseRedirect(reverse('cars:car_list'))
		else:
			return render(request, 'app01/search.html', context={'form':form})
	else:
		form = SearchForm()
		return render(request, 'app01/search.html', context={'form': form})


def main_carlist(request):
	cars = Vehicles.objects.filter(country='ru')
	cars_de = Vehicles.objects.filter(country='de')
	return render(request, 'app01/car_list.html', context={'cars': cars, 'cars_de': cars_de})

class IndexView(TemplateView):
	template_name = 'app01/index.html'


class CarListView(ListView):
	model = Vehicles
	template_name = 'app01/car_list.html'

	def get_context_data(self, *args, **kwargs):
		context=super().get_context_data(*args, **kwargs)
		context['title'] = 'Список машин'
		return context

	def get_queryset(self):
		return Vehicles.objects.all()


class CarDetailView(DetailView):
	model = Vehicles
	template_name = 'app01/car_detail.html'

	def get(self,request,  *args, **kwargs):
		self.v_id = kwargs['pk']
		return super().get(request, *args, **kwargs)


	def get_context_data(self, *args, **kwargs):
		context=super().get_context_data(*args, **kwargs)
		context['title'] = 'Автомобиль'
		return context

	def get_object(self, queryset=None):
		return get_object_or_404(Vehicles, pk = self.v_id)


class CarCreateView(CreateView):
	fields = "__all__"
	model = Vehicles
	success_url = reverse_lazy('cars:index')
	template_name = 'app01/car_create.html'

	def post(self, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):
		return super().form_valid(self, form)


class CarUpdateView(UpdateView):
	fields = "__all__"
	model = Vehicles
	success_url = reverse_lazy('cars:index')
	template_name = 'app01/car_create.html'

class CarDeleteView(DeleteView):
	template_name = 'app01/car_delete_confirm.html'
	model = Vehicles
	success_url = reverse_lazy('cars:car_list')

# def new(request):
# 	if request.method == 'GET':
# 		form = VehicleForm()
# 		return render(request, 'app01/new.html', context={'form': form})
# 	else:
# 		form = VehicleForm(request.POST, files=request.FILES )
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect(reverse('cars:index'))
# 		else:
# 			return render(request, 'app01/new.html', context={'form': form})

# def main_view(request):
# 	cars = Vehicles.objects.all()
# 	return render(request, 'app01/index.html', context = {'cars': cars})
