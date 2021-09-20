from django.contrib import admin
from django.urls import path, include
add_app='main'
urlpatterns = [
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls)
]