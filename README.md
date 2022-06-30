
# TuxPizzas

Una App de pizzas hecha con Python, usando el Django como framework


## App Demo

![App Screenshot](https://media.giphy.com/media/w0Hp1hscHMZnOVsGTb/giphy.gif)


## Documentation

Creacion de projeto django 

Creacion de app django

Utilizo una plantilla de bootstrap modificada y adaptada a la necesidad, en la cual renderizo los datos desde el backend, usando la herencia de padre a hijo para altenar las diferentes vistas que cree desde ahi.

## models.py
En este archivo se encuentra el modelaje de datos de la tabla , Pizzas , Empanadas y Hamburguesas.

## forms.py 
En este archivo se encuentra el formulario que hace envio de los datos ingresados al backend.

## views.py
Aca encontraremos las vistas creadas y moldeadas para la navegacion de la web.

## urls.py

Archivo donde esta la configuracion de rutas.

## Inicio

En esta page podemos encontrar un viztaso general de la web, ver algunos productos traidos directamente de la db.

## Productos
Aca podes ir a la seccion correspondiente por cada categoria, y asi encontrar los productos de la misma.

## Crear Producto

En este menu podes elegir que producto crear, ya sea pizza, empanada o hamburguesa, estos datos que se cargan a la base de datos, a travez del modelo y del form para asi renderizar los productos cargados.

## Buscar pizza

Aca podes buscar alguna pizza en particular, usando el nombre del mismo, consulta la informacion con la base de datos y la compara, si no encuentra lo solicitado, da un aviso de que ingrese un dato valido, caso contrario renderiza el producto solicitado.


## Authors

- [@Fernando Alarcon](https://www.linkedin.com/in/feralarcon1995/)

