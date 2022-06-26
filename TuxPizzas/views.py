from django.http import HttpResponse
from django.shortcuts import render
from TuxPizzas.models import Pizzas

# Create your views here.

def pizzas(self):

    pizza =  Pizzas(nombre="Especial Tux", tamanio="Familiar", ingredientes= "Jamon , Morron, Ajo y albahaca", precio= 1300)
    pizza.save()
    documento = f"Pizza: {pizza.nombre}, Tamaño: {pizza.tamanio}, Ingredientes: {pizza.ingredientes}, Precio:{pizza.precio}"

    return HttpResponse(documento)

def inicio(request):

    return render(request,"TuxPizzas/inicio.html")

def productos(request):

    return render(request,"TuxPizzas/productos.html")

def servicios(request):

    return render(request,"TuxPizzas/servicios.html")        

def pizzas(request):

    return render(request,"TuxPizzas/pizzas.html")        

def empanadas(request):

    return render(request,"TuxPizzas/empanadas.html")                