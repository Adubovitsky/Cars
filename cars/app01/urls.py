from django.urls import path
from app01 import views

app_name = 'app01'

urlpatterns =\
    [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.contacts, name = 'contact'),
    path('search/', views.search, name = 'search'),
    # path('filter-list/', views.CarListView.as_view(), name = 'filter_list'),
    path('filter-list/', views.filter, name = 'filter_list'),
    path('car-list/', views.main_carlist, name = 'car_list'),
    path('car-detail/<int:pk>/', views.CarDetailView.as_view(), name = 'car_detail'),
    path('car-create/', views.CarCreateView.as_view(), name = 'car_create'),
    path('car-update/<int:pk>/', views.CarUpdateView.as_view(), name = 'car_update'),
    path('car-delete/<int:pk>/', views.CarDeleteView.as_view(), name = 'car_delete'),
    path('order-create/', views.new_order, name = 'order_create'),
    path('test/', views.test, name='test'),
    path('summary/', views.summary, name='summary'),
   ]
