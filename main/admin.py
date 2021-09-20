from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationsForm
from .models import Absuser, Card

class CustomUserAdmin(UserAdmin):
    model = Absuser
    add_form = CustomUserCreationsForm

admin.site.register(Absuser, CustomUserAdmin)
admin.site.register(Card)
