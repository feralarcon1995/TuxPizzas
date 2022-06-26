from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.

class Pizzas(models.Model):

    nombre = models.CharField(max_length=30)
    tamanio = models.CharField(max_length=10)
    ingredientes = models.CharField(max_length=60)
    precio = models.IntegerField() 


class Empanadas(models.Model):

    nombre = models.CharField(max_length=30)
    cantidad = models.IntegerField() 
    precio = models.IntegerField() 