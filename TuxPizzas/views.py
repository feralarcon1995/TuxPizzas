from django.http import HttpResponse
from django.shortcuts import render
from TuxPizzas.models import *
from TuxPizzas.forms import *

# Create your views here.

def inicio(request):
    tuxpizza = Pizzas.objects.all()
    contexto= {'pizzas':tuxpizza} 
 
    return render(request,"TuxPizzas/inicio.html",contexto)

def pizzas(request):

    tuxpizza = Pizzas.objects.all()
    contexto= {'pizzas':tuxpizza}

    return render(request,"TuxPizzas/pizzas.html", contexto)        

def empanadas(request):

    tuxpizza = Empanadas.objects.all()
    contexto= {'empanadas':tuxpizza}

    return render(request,"TuxPizzas/empanadas.html", contexto)       


def hamburguesas(request):

    tuxpizza = Hamburguesas.objects.all()
    contexto= {'hamburguesas':tuxpizza}

    return render(request,"TuxPizzas/hamburguesas.html", contexto)           


def crearPizza(request):

   if request.method == "POST":

        miFormulario = PizzaFormulario(request.POST)

        print(miFormulario)

        if PizzaFormulario.is_valid:

           informacion = miFormulario.cleaned_data

           pizza = Pizzas (nombre=informacion['nombre'],foto=informacion['foto'], tamanio=informacion['tamanio'], ingredientes=informacion['ingredientes'], precio=informacion['precio'])

           pizza.save()

           return render(request, "TuxPizzas/inicio.html")    

   else:

      miFormulario= PizzaFormulario()

   return render(request,'TuxPizzas/formulario.html',{"miFormulario":miFormulario}) 

def crearEmpanada(request):

   if request.method == "POST":

        miFormulario = EmpanadasFormulario(request.POST)

        print(miFormulario)

        if EmpanadasFormulario.is_valid:

           informacion = miFormulario.cleaned_data

           empanadas = Empanadas(nombre=informacion['nombre'],foto=informacion['foto'], relleno=informacion['relleno'], precio=informacion['precio'])

           empanadas.save()

           return render(request, "TuxPizzas/inicio.html")    

   else:

      miFormulario= EmpanadasFormulario()

   return render(request,'TuxPizzas/formEmpanada.html',{"miFormulario":miFormulario})  

def crearHamburguesa(request):

   if request.method == "POST":

        miFormulario = HamburguesasFormulario(request.POST)

        print(miFormulario)

        if HamburguesasFormulario.is_valid:

           informacion = miFormulario.cleaned_data

           hamburguesa = Hamburguesas(nombre=informacion['nombre'],foto=informacion['foto'], ingredientes=informacion['ingredientes'], precio=informacion['precio'])

           hamburguesa.save()

           return render(request, "TuxPizzas/inicio.html")    

   else:

      miFormulario= HamburguesasFormulario()

   return render(request,'TuxPizzas/formHamburguesa.html',{"miFormulario":miFormulario})        


def buscarPizza(request):

    return render(request, "TuxPizzas/buscarPizza.html")

def buscar(request):

    if request.GET['nombre']:
       nombre = request.GET['nombre']
       pizzas = Pizzas.objects.filter(nombre__icontains=nombre)
       
       return render(request,"TuxPizzas/resultadosBusqueda.html",{"pizzas": pizzas,"nombre":nombre})

    else:
      
      respuesta = "No enviaste datos"

    return HttpResponse(respuesta)
