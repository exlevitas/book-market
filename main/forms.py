from django.contrib.auth.forms import UserCreationForm
from .models import Absuser
from .models import Card
from django.forms import ModelForm
from django import forms

class CustomUserCreationsForm(UserCreationForm):
    class Meta:
        model = Absuser
        fields = '__all__'


class CardForms(ModelForm):
    class Meta:
        model = Card
        fields = ('title', 'content', 'price')
