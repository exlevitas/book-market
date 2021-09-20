
from django.contrib import admin
from django.urls import path
from main.views import index, CardCreateView

urlpatterns = [
    path('', index),
    path('page1/',CardCreateView.as_view(),name='name'),

]