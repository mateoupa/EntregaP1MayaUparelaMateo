from django.urls import URLPattern, path

from .views import inicio , registroauditor,registro_productos,registroalmacen

urlpatterns = [
    path('',inicio, name= 'base'),
    path('auditor/',registroauditor, name= 'registro_auditor'),
    path('producto/',registro_productos, name= 'registro_producto'),
    path('almacen/',registroalmacen, name= 'registro_almacen')
    
    
]
