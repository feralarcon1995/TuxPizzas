from django.http import HttpResponse
from django.shortcuts import render

from TuxPizzas.models import Pizzas

# Create your views here.

def pizzas(self):

    pizza =  Pizzas(nombre="Especial Tux", tamanio="Familiar", ingredientes= "Jamon , Morron, Ajo y albahaca", precio= 1300)
    pizza.save()
    documento = f"Pizza: {pizza.nombre}, Tamaño: {pizza.tamanio}, Ingredientes: {pizza.ingredientes}, Precio:{pizza.precio}"

    return HttpResponse(documento)