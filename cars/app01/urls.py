from django.urls import path
from app01 import views

app_name = 'app01'

urlpatterns = [path('', views.main_view, name ='index' ),
                path('contact/', views.contacts, name = 'contact'),
               path('search/', views.search, name = 'search')
               ]
