from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('informacionCanina/', views.informacionCanina, name='informacionCanina'),
    path('contacto/', views.contacto, name='contacto'),
    path('movil/', views.movil, name='movil'),
    path('iot/', views.iot, name='iot')

    
]