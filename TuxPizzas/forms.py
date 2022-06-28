from django import forms


class PizzaFormulario(forms.Form):
    TAMANIO_OPCIONES = (
    (1, "Individual"),
    (2, "Grande"),
    (3, "Familiar"),
    )
  
    nombre = forms.CharField(max_length=30)
    foto = forms.CharField(max_length=9999999)
    tamanio = forms.ChoiceField(choices=TAMANIO_OPCIONES)
    ingredientes = forms.CharField(max_length=60) 
    precio = forms.IntegerField()   

class EmpanadasFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    foto = forms.CharField(max_length=9999999)     
    relleno = forms.CharField(max_length=50)
    precio = forms.IntegerField() 

class HamburguesasFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    foto = forms.CharField(max_length=9999999)     
    ingredientes= forms.CharField(max_length=50)
    precio = forms.IntegerField()   


