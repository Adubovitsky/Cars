from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.paginator import Paginator
from django.views.generic.base import ContextMixin
from .models import Vehicles, Orders
from .forms import ContactForm, VehicleForm, SearchForm, OrdernewForm
from django.core.mail import send_mail
from django.core.management import commands, call_command
from app01.management.commands import filldb
from django.db.models import Avg
from.filters import VehicleFilter


# Create your views here.

def test (request):
	context = {}
	cars = Vehicles.objects_de.all()
	context['cars'] = cars
	context['test'] ='надпись для теста'
	return render(request, 'app01/test.html', context=context)

def filter(request):
	context={}

	filtered_vehicles = VehicleFilter(request.GET, queryset=Vehicles.objects.all())
	context['filtered_cars'] = filtered_vehicles

	paginated_filtered_vehicles = Paginator(filtered_vehicles.qs, 9)
	page_number = request.GET.get('page')
	car_page_obj = paginated_filtered_vehicles.get_page(page_number)
	context['car_page_obj'] = car_page_obj

	return render(request, 'app01/filter_list.html', context = context)


def summary (request):
	def count(year, km):
		return Vehicles.objects_rus.filter(pr_year__pr_year=year, milage__mil_group=km).count()

	def avg_price(year, km):
		return Vehicles.objects_rus.filter(pr_year__pr_year=year, milage__mil_group = km).aggregate(Avg('price'))['price__avg']

	def count_de(year, km):
		return Vehicles.objects_de.filter(pr_year__pr_year=year, milage__mil_group=km).count()

	def avg_price_de(year, km):
		return Vehicles.objects_de.filter(pr_year__pr_year=year, milage__mil_group = km).aggregate(Avg('price'))['price__avg']

	context = {}
	context['test']=Vehicles.objects_rus.all().count()
	context['num_de'] = Vehicles.objects_de.all().count()
	context['car'] = Vehicles.objects_rus.all().first()
	context['quant_rus22_30'] = count(2022, 'до 30')
	context['price_rus22_30'] = avg_price( 2022, 'до 30')
	context['quant_rus22_70'] = count(2022, 'до 70')
	context['price_rus22_70'] = avg_price(2022, 'до 70')
	context['quant_rus22_120'] = count(2022, 'до 120')
	context['price_rus22_120'] = avg_price(2022, 'до 120')
	context['quant_rus21_30'] = count(2021, 'до 30')
	context['price_rus21_30'] = avg_price(2021, 'до 30')
	context['quant_rus21_70'] = count(2021, 'до 70')
	context['price_rus21_70'] = avg_price(2021, 'до 70')
	context['quant_rus21_120'] = count(2021, 'до 120')
	context['price_rus21_120'] = avg_price(2021, 'до 120')
	context['quant_rus20_30'] = count(2020, 'до 30')
	context['price_rus20_30'] = avg_price(2020, 'до 30')
	context['quant_rus20_70'] = count(2020, 'до 70')
	context['price_rus20_70'] = avg_price(2020, 'до 70')
	context['quant_rus20_120'] = count(2020, 'до 120')
	context['price_rus20_120'] = avg_price(2020, 'до 120')
	context['quant_rus19_30'] = count(2019, 'до 30')
	context['price_rus19_30'] = avg_price(2019, 'до 30')
	context['quant_rus19_70'] = count(2019, 'до 70')
	context['price_rus19_70'] = avg_price(2019, 'до 70')
	context['quant_rus19_120'] = count(2019, 'до 120')
	context['price_rus19_120'] = avg_price(2019, 'до 120')
	context['quant_rus18_30'] = count(2018, 'до 30')
	context['price_rus18_30'] = avg_price(2018, 'до 30')
	context['quant_rus18_70'] = count(2018, 'до 70')
	context['price_rus18_70'] = avg_price(2018, 'до 70')
	context['quant_rus18_120'] = count(2018, 'до 120')
	context['price_rus18_120'] = avg_price(2018, 'до 120')

	context['quant_eu22_30'] = count_de(2022, 'до 30')
	context['price_eu22_30'] = avg_price_de(2022, 'до 30')
	context['quant_eu22_70'] = count_de(2022, 'до 70')
	context['price_eu22_70'] = avg_price_de(2022, 'до 70')
	context['quant_eu22_120'] = count_de(2022, 'до 120')
	context['price_eu22_120'] = avg_price_de(2022, 'до 120')
	context['quant_eu21_30'] = count_de(2021, 'до 30')
	context['price_eu21_30'] = avg_price_de(2021, 'до 30')
	context['quant_eu21_70'] = count_de(2021, 'до 70')
	context['price_eu21_70'] = avg_price_de(2021, 'до 70')
	context['quant_eu21_120'] = count_de(2021, 'до 120')
	context['price_eu21_120'] = avg_price_de(2021, 'до 120')
	context['quant_eu20_30'] = count_de(2020, 'до 30')
	context['price_eu20_30'] = avg_price_de(2020, 'до 30')
	context['quant_eu20_70'] = count_de(2020, 'до 70')
	context['price_eu20_70'] = avg_price_de(2020, 'до 70')
	context['quant_eu20_120'] = count_de(2020, 'до 120')
	context['price_eu20_120'] = avg_price_de(2020, 'до 120')
	context['quant_eu19_30'] = count_de(2019, 'до 30')
	context['price_eu19_30'] = avg_price_de(2019, 'до 30')
	context['quant_eu19_70'] = count_de(2019, 'до 70')
	context['price_eu19_70'] = avg_price_de(2019, 'до 70')
	context['quant_eu19_120'] = count_de(2019, 'до 120')
	context['price_eu19_120'] = avg_price_de(2019, 'до 120')
	context['quant_eu18_30'] = count_de(2018, 'до 30')
	context['price_eu18_30'] = avg_price_de(2018, 'до 30')
	context['quant_eu18_70'] = count_de(2018, 'до 70')
	context['price_eu18_70'] = avg_price_de(2018, 'до 70')
	context['quant_eu18_120'] = count_de(2018, 'до 120')
	context['price_eu18_120'] = avg_price_de(2018, 'до 120')

	return render(request, 'app01/summary.html', context=context)

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
			return HttpResponseRedirect(reverse('cars:summary'))
		else:
			return render(request, 'app01/search.html', context={'form':form})
	else:
		form = SearchForm()
		return render(request, 'app01/search.html', context={'form': form})


def main_carlist(request):
	cars = Vehicles.objects.filter(country='ru')
	paginator = Paginator(cars, 10)  # Show 15 contacts per page.
	page_number = request.GET.get('page')
	cars_page = paginator.get_page(page_number)
	cars_de = Vehicles.objects.filter(country='de')
	paginator = Paginator(cars_de, 10)
	page_number = request.GET.get('page')
	carsde_page = paginator.get_page(page_number)

	return render(request, 'app01/car_list.html', context={'cars': cars_page, 'cars_de': carsde_page})

class IndexView(TemplateView):
	template_name = 'app01/index.html'

# class CarListView(ListView):
# 	paginate_by = 15
# 	model = Vehicles
# 	template_name = 'app01/filter_list.html'
#
# 	def __init__(self):
# 		self.filter = 2022
#
# 	def get_context_data(self, *args, **kwargs):
# 		context=super().get_context_data(*args, **kwargs)
# 		context['title'] = 'Список машин'
# 		context['test'] = self.request.GET.get('year', None)
# 		return context
#
# 	def get_queryset(self):
# 		def get_input():
# 			if self.request.GET.get('year') != None:
# 				year = self.request.GET.get('year')
# 				self.filter = int(year)
# 				return self.filter
# 		get_input()
# 		return Vehicles.objects_rus.filter(pr_year__pr_year = self.filter)


class CarDetailView(LoginRequiredMixin, DetailView):
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


class CarUpdateView(UserPassesTestMixin,UpdateView):
	fields = "__all__"
	model = Vehicles
	success_url = reverse_lazy('cars:index')
	template_name = 'app01/car_create.html'

	def test_func(self):
		return self.request.user.is_superuser

class CarDeleteView(UserPassesTestMixin,DeleteView):
	template_name = 'app01/car_delete_confirm.html'
	model = Vehicles
	success_url = reverse_lazy('cars:car_list')

	def test_func(self):
		return self.request.user.is_superuser



@login_required
def new_order(request):
	if request.method == 'GET':
		form = OrdernewForm()
		return render(request, 'app01/order_create.html', context={'form': form})
	else:
		form = OrdernewForm(request.POST, files=request.FILES )
		if form.is_valid():
			form.instance.user = request.user
			form.save()
			return HttpResponseRedirect(reverse('cars:index'))
		else:
			return render(request, 'app01/order_create.html', context={'form': form})


# class OrderCreateView(CreateView):
# 	fields = "__all__"
# 	model = Orders
# 	success_url = reverse_lazy('cars:index')
# 	template_name = 'app01/order_create.html'
#
# 	def post(self, request, *args, **kwargs):
# 		return super().post(request, *args, **kwargs)
#
# 	def form_valid(self, form):
# 		return super().form_valid(self, form)


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


#

# >>> Vehicles.objects.filter(production_year__production_year=2020)
