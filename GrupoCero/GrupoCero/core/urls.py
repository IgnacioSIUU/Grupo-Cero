from xml.etree.ElementInclude import include
from django.db import router
from django.urls import path
from .views import home,contacto,main_pinturas,Inf_imagen2,Inf_imagen,Inf_imagen3,Inf_imagen4,main_esculturas,main_orfebreria,escultura1,escultura2,agregar_arte,listar_artes,mod_arte,del_arte,\
    registro,lista_artes,orfebreria1,orfebreria2,orfebreria3,orfebreria4,detalle_arte,ConoceMas
from .viewslogin import loginapi



urlpatterns = [
    path('', home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('ConoceMas',ConoceMas,name="ConoceMas"),
    path('main_pinturas/',main_pinturas,name="main_pinturas"),
    path('main_esculturas/',main_esculturas,name="main_esculturas"),
    path('escultura1',escultura1,name="escultura1"),
    path('escultura2',escultura2,name="escultura2"),
    path('main_orfebreria/',main_orfebreria,name="main_orfebreria"),
    path('orfebreria1',orfebreria1,name="orfebreria1"),
    path('orfebreria2',orfebreria2,name="orfebreria2"),
    path('orfebreria3',orfebreria3,name="orfebreria3"),
    path('orfebreria4',orfebreria4,name="orfebreria4"),
    path('Inf_imagen',Inf_imagen,name="Inf_imagen"),
    path('Inf_imagen2',Inf_imagen2,name="Inf_imagen2"),
    path('Inf_imagen3',Inf_imagen3,name="Inf_imagen3"),
    path('Inf_imagen4',Inf_imagen4,name="Inf_imagen4"),
    path('agregar_arte/',agregar_arte,name="agregar_arte"),
    path('mod_arte/<id>/',mod_arte,name="mod_arte"),
    path('del_arte/<id>/',del_arte,name="del_arte"),
    path('registro',registro,name="registro"),
    path('listar_artes/',listar_artes,name="listar_artes"),
    path('lista_artes/',lista_artes,name="lista_artes"),
    path('detalle_arte/<id>',detalle_arte,name="detalle_arte"),
    path('loginapi',loginapi,name="loginapi"),
]