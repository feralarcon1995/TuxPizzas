from django.urls import path
from TuxPizzas import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('pizzas', views.pizzas, name="Pizzas"),
    path('hamburguesas', views.hamburguesas, name="Hamburguesas"),
    path('empanadas', views.empanadas, name="Empanadas"),
    path('formulario', views.crearPizza, name="Formulario"),
    path('formulario_empanadas', views.crearEmpanada, name="FormularioEmpanadas"),
    path('formulario_hamburguesa', views.crearHamburguesa, name="FormularioHamburguesas"),
    path('buscarPizza', views.buscarPizza, name="BuscarPizza"),
    path('buscar/', views.buscar)

]
