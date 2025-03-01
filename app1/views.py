from django.shortcuts import render
from django.views.generic import  TemplateView
   

def hola_mundo (request):
    return render(request, 'adios_mundo')

class adios_mundo(TemplateView):
    template_name = 'adiosChao.html'