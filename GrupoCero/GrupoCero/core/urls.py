from django.urls import path
from .views import home,contacto,main_pinturas,Inf_imagen2,main_esculturas,main_orfebreria,escultura1,escultura2,agregar_arte,listar_artes,mod_arte,del_arte,\
    registro

urlpatterns = [
    path('', home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('main_pinturas/',main_pinturas,name="main_pinturas"),
    path('main_esculturas/',main_esculturas,name="main_esculturas"),
    path('escultura1',escultura1,name="escultura1"),
    path('escultura2',escultura2,name="escultura2"),
    path('main_orfebreria/',main_orfebreria,name="main_orfebreria"),
    path('Inf_imagen2',Inf_imagen2,name="Inf_imagen2"),
    path('agregar_arte/',agregar_arte,name='agregar_arte'),
    path('listar_artes/',listar_artes,name="listar_artes"),
    path('mod_arte/<id>/',mod_arte,name="mod_arte"),
    path('del_arte/<ID>/',del_arte,name="del_arte"),
    path('registro',registro,name="registro"),
]