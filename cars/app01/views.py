from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.paginator import Paginator
from django.views.generic.base import ContextMixin
from .models import Vehicles, Orders, Age, Mileage, Milgr, Location
from .forms import ContactForm, VehicleForm, SearchForm, OrdernewForm
from django.core.mail import send_mail
from django.core.management import commands, call_command
from app01.management.commands import filldb
from django.db.models import Avg, Count
from .filters import VehicleFilter
from django_pivot.pivot import pivot
import pandas as pd

# Create your views here.

def test (request):
	context = {}
	# pv = pivot(Vehicles, ['country', 'pr_year'], 'milgr', 'price', aggregation=Count, default=0)
	# context['carsde'] = Vehicles.objects_de.all().first()
	# query = Vehicles.objects.select_related('country').all()
	# context['test']= Vehicles.objects.filter(country__name = 'Россия').aggregate(Count('id'), Avg('price'))
	# context['test1'] = Vehicles.objects.filter(country__name='Европа').aggregate(Count('id'), Avg('price'))
	# context['num_de'] = query.filter(country__name = 'Европа').count()
	# context['carrus'] = Vehicles.objects_rus.all().first()
	return render(request, 'app01/test.html', context)

def filter(request):
	context={}

	filtered_vehicles = VehicleFilter(request.GET, queryset=Vehicles.objects.select_related('pr_year','milage','country').all())
	context['filtered_cars'] = filtered_vehicles

	paginated_filtered_vehicles = Paginator(filtered_vehicles.qs, 9)
	page_number = request.GET.get('page')
	car_page_obj = paginated_filtered_vehicles.get_page(page_number)
	context['car_page_obj'] = car_page_obj

	return render(request, 'app01/filter_list.html', context = context)


def summary (request):
	context = {}
	pv = pivot(Vehicles, ['country', 'pr_year'], 'milgr', 'price', aggregation=Count, default=0)
	var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12 = pv
	lvar1 = list(var1.values())
	lvar2 = list(var2.values())
	lvar3 = list(var3.values())
	lvar4 = list(var4.values())
	lvar5 = list(var5.values())
	lvar6 = list(var6.values())
	lvar7 = list(var7.values())
	lvar8 = list(var8.values())
	lvar9 = list(var9.values())
	lvar10 = list(var10.values())
	lvar11 = list(var11.values())
	lvar12 = list(var12.values())
	context['pv'] = pv
	context['q_rus_22'] = lvar1
	context['q_rus_21'] = lvar2
	context['q_rus_20'] = lvar3
	context['q_rus_19'] = lvar4
	context['q_rus_18'] = lvar5
	context['q_de_22'] = lvar7
	context['q_de_21'] = lvar8
	context['q_de_20'] = lvar9
	context['q_de_19'] = lvar10
	context['q_de_18'] = lvar11

	pv = pivot(Vehicles, ['country', 'pr_year'], 'milgr', 'price', aggregation=Avg, default=0.0)
	vr1, vr2, vr3, vr4, vr5, vr6, vr7, vr8, vr9, vr10, vr11, vr12 = pv
	lvr1 = list(vr1.values())
	lvr2 = list(vr2.values())
	lvr3 = list(vr3.values())
	lvr4 = list(vr4.values())
	lvr5 = list(vr5.values())
	lvr6 = list(vr6.values())
	lvr7 = list(vr7.values())
	lvr8 = list(vr8.values())
	lvr9 = list(vr9.values())
	lvr10 = list(vr10.values())
	lvr11 = list(vr11.values())
	lvr12 = list(vr12.values())
	context['pv'] = pv
	context['p_rus_22'] = lvr1
	context['p_rus_21'] = lvr2
	context['p_rus_20'] = lvr3
	context['p_rus_19'] = lvr4
	context['p_rus_18'] = lvr5
	context['p_de_22'] = lvr7
	context['p_de_21'] = lvr8
	context['p_de_20'] = lvr9
	context['p_de_19'] = lvr10
	context['p_de_18'] = lvr11

	context['car'] = Vehicles.objects_rus.all().first()
	return render(request, 'app01/summary.html', context)

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
			Age.objects.all().delete()
			Mileage.objects.all().delete()
			Location.objects.all().delete()
			Milgr.objects.all().delete()
			brand = form.cleaned_data['car_brand']
			model = form.cleaned_data['car_model']
			call_command('fill_dict')
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
