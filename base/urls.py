from django.urls import URLPattern, path
from .views import inicio

urlpatterns = [
    path('',inicio, name= 'base')
]
