from django.shortcuts import render
from django.http import HttpResponse

from portfolio.models import Project

# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def informacionCanina(request):
    return render(request, 'core/informacionCanina.html')

def movil(request):
    return render(request, 'core/movil.html')

def iot(request):
    return render(request, 'core/iot.html')

def contacto(request):
    return render(request, 'core/contacto.html')