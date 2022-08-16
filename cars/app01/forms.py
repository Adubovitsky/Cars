from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Имя")
    email = forms.EmailField(label="email")
    message = forms.CharField(label="Сообщение")