from django.urls import path
from TuxPizzas import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('productos', views.productos, name="Productos"),
    path('servicios', views.servicios, name="Servicios"),
    path('pizzas', views.pizzas, name="Pizzas"),
    path('empanadas', views.empanadas, name="Empanadas"),

]
