from django.shortcuts import render
from main.models import Card
from .forms import CardForms
from django.views.generic import CreateView

# Create your views here.

#from django.http import HttpResponse
#from .models import Card
#def index(request):
#    s = 'Список товаров\r\n\r\n\r\n'
#    for f in Card.objects.order_by('-published'):
#        s += f.title + '\r\n' + f.content + '\r\n\r\n'
#    return HttpResponse(s, content_type='text/plain;charset=utf-8')

def index(request):
    t = Card.objects.all()
    content = {'t':t}
    return render(request, 'main/basic.html', content)

# def page1(request):
#     t = Card.objects.all()
#     content = {'t': t}
#     return render(request, 'main/index1.html', content)

class CardCreateView(CreateView):
    template_name = 'main/index1.html'
    form_class = CardForms
    success_url = '/main/'