from django.urls import path
from usersapp import views
from django.contrib.auth.views import LoginView

app_name = 'app01'

urlpatterns =\
    [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    ]