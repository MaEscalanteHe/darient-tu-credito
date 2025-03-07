from django.urls import path
from . import views

urlpatterns = [
    # Root page.
    path('', views.home, name='home'),

    # Bank related URLs.
    path('bancos/', views.bank, name='banks'),
    path('bancos/agregar', views.addBank, name='addBank'),

    # Client related URLs.
    path('clientes/', views.client, name='clients'),
    path('clientes/<int:client_id>/', views.viewClient, name='viewClient'),
    path('clientes/agregar', views.addClient, name='addClient'),
    path('clientes/editar/<int:client_id>/', views.updateClient, name='updateClient'),
    path('clientes/eliminar/<int:client_id>/', views.removeClient, name='removeClient'),

    # Credit related URLs.
    path('creditos/', views.credit, name='credits'),
    path('creditos/agregar', views.addCredit, name='addCredit')
]