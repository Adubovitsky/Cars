from django.contrib.auth.forms import UserCreationForm
from .models import SiteUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = ('username', 'password1','password2', 'email')