from django.http import HttpResponse
from django.shortcuts import render
from base.forms import registro_auditor, registroproducto,registro_almacen,busqueda_producto
from base.models import auditor,registro_producto,almacen


# Create your views here.


def inicio(request):
    
    return render(request,'Principal/index.html',{})



def registroauditor(request):
    
# con formulario de django
    if request.method =='POST':
        formulario = registro_auditor(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            modelo_auditor = auditor(nombre=data['nombre'],cargo=data['cargo'],email=data['email'])
            modelo_auditor.save()
            return render(request,'Principal/auditor.html',{'modelo_auditor':modelo_auditor})   
            
                
    formulario_auditor = registro_auditor()
    return render(request,'Principal/auditor.html',{'formulario_auditor':formulario_auditor})


def registro_productos(request):
    
# con formulario de django
    if request.method =='POST':
        formulario_producto = registroproducto(request.POST)
        if formulario_producto.is_valid():
            data = formulario_producto.cleaned_data
            modelo_producto = registro_producto(nombre=data['nombre'],precio=data['precio'],cantidad=data['cantidad'])
            modelo_producto.save()
            return render(request,'Principal/producto.html',{'modelo_producto':modelo_producto})   
            
                
    formularioproducto = registroproducto()
    return render(request,'Principal/producto.html',{'formularioproducto':formularioproducto})



def registroalmacen(request):
    
# con formulario de django
    if request.method =='POST':
        formulario_almacen = registro_almacen(request.POST)
        if formulario_almacen.is_valid():
            data = formulario_almacen.cleaned_data
            modelo_almacen = almacen(nombre=data['nombre'],turno=data['turno'])
            modelo_almacen.save()
            return render(request,'Principal/almacen.html',{'modelo_almacen':modelo_almacen})   
            
                
    formularioalmacen = registro_almacen()
    return render(request,'Principal/almacen.html',{'formularioalmacen':formularioalmacen})


def busquedaproducto(request):
    
    productos_buscados=[]
    dato=request.GET.get('partial_producto',None)
    
    if dato is not None:
        productos_buscados=registro_producto.objects.filter(nombre__icontains=dato)
    
    buscador=busqueda_producto()
    return render(request,'Principal/busqueda_producto.html',{'buscador':buscador,'productos_buscados':productos_buscados})