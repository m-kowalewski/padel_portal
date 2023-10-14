from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, EmailField
from .models import Player


class PlayerCreationForm(UserCreationForm):
    class Meta:
        model = Player
        fields = ["username", "password1", "password2", "first_name", "email"]

    email = EmailField(required=True)


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ["username", "first_name", "email"]
