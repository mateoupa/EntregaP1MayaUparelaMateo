
from django import forms


class registro_auditor(forms.Form):
    nombre = forms.CharField(max_length=20)
    cargo = forms.CharField(max_length=20)
    email = forms.CharField()
    

class registroproducto(forms.Form):
    nombre = forms.CharField(max_length=20)
    precio = forms.IntegerField()
    cantidad =forms.IntegerField()
    
    
class registro_almacen(forms.Form):
    nombre = forms.CharField(max_length=20)
    turno = forms.IntegerField()