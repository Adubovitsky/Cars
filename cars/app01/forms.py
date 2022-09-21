from django import forms
from .models import Vehicles, Orders

class ContactForm(forms.Form):
    name = forms.CharField(label="Имя")
    email = forms.EmailField(label="email")
    message = forms.CharField(label="Сообщение")


class VehicleForm(forms.ModelForm):
    brand = forms.CharField(label="Название", widget=forms.TextInput(attrs={'placeholder': 'Мерседес', 'class': 'form-control'}))
    class Meta:
        model = Vehicles

        # fields = '__all__'
        exclude = ('engine',)


class SearchForm(forms.Form):
    car_brand = forms.CharField(label = "Марка автомобиля", widget=forms.TextInput(attrs={'placeholder':'kia'}))
    car_model = forms.CharField(label="Модель", widget=forms.TextInput(attrs={'placeholder':'sportage'}))

class FilterForm(forms.Form):
    year = forms.CharField(label = "Год выпуска", widget=forms.TextInput(attrs={'placeholder':'2022'}))
    miles = forms.CharField(label="Пробег", widget=forms.TextInput(attrs={'placeholder':'20000'}))

# class OrderForm(forms.Form):
#     name = forms.CharField(label="Имя")
#     email = forms.EmailField(label="email")
#     message = forms.CharField(label="Сообщение")

class OrdernewForm(forms.ModelForm):
    name = forms.CharField(label='Тема')
    text = forms.CharField(label='Применое описание машины для подбора', widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Orders
        # fields = '__all__'
        exclude = ('user',)