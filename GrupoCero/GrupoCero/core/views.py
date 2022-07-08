from django.shortcuts import render,redirect,get_object_or_404
from .models import Arte
from .forms import ContactoForm,ArteForm,CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required,permission_required
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt 
from rest_framework import viewsets
from .serializers import ArteSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




# Create your views here.



def home(request):
    artes = Arte.objects.all()
    data = {
        'artes': artes
    }
    return render(request,'app/home.html',data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "enviado correctamente"
        else:
            data["form"] = formulario
    return render (request,'app/contacto.html',data)

def main_pinturas(request):
    return render (request,'app/main_pinturas.html')

def Inf_imagen(request):
    return render (request,'app/Inf_imagen.html')

def Inf_imagen2(request):
    return render (request,'app/Inf_imagen2.html')

def Inf_imagen3(request):
    return render (request,'app/Inf_imagen3.html')

def Inf_imagen4(request):
    return render (request,'app/Inf_imagen4.html')

def main_esculturas(request):
    return render (request,'app/main_esculturas.html')

def main_orfebreria(request):
    return render (request,'app/main_orfebreria.html')

def orfebreria1(request):
    return render(request,'app/arteshtmls/orfebreriashtml/orfebreria1.html')

def orfebreria2(request):
    return render(request,'app/arteshtmls/orfebreriashtml/orfebreria2.html')

def orfebreria3(request):
    return render(request,'app/arteshtmls/orfebreriashtml/orfebreria3.html')
    
def orfebreria4(request):
    return render(request,'app/arteshtmls/orfebreriashtml/orfebreria4.html')
    
def escultura1(request):
    return render (request,'app/arteshtmls/esculturashtmls/escultura1.html')

def escultura2(request):
    return render (request,'app/arteshtmls/esculturashtmls/escultura2.html')

def ConoceMas(request):
    return render (request,'app/ConoceMas.html')


@permission_required('core.add_arte')
@login_required
def agregar_arte(request):
    data = {
        'form':ArteForm()
    }
    if request.method == 'POST':
        formulario = ArteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "PRODUCTO AGREGADO CORRECTAMENTE"
        else:
            data["form"] = formulario
    return render(request,'app/artes/agregar.html',data)

@permission_required('core.view_arte')
def listar_artes(request):
    artes = Arte.objects.all()

    data = {
        'artes':artes
    }
    return render(request,'app/artes/listar.html',data)

@permission_required('core.change_arte')
def mod_arte(request,id):
    arte = Arte.objects.get(idprod=id)
    data = {
        'form': ArteForm(instance=Arte)
    }
    if request.method=='POST':
        formulario=ArteForm(data=request.POST, instance=arte)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"MODIFICADO CORRECTAMENTE")
            return redirect(to="listar_artes")
        data["form"]=formulario
    return render(request,'app/artes/mod.html',data)

@permission_required('core.delete_arte')
def del_arte(request, id):
    arte = Arte.objects.get(idprod=id)
    arte.delete()
    messages.success(request,"ELIMINADO CORRECTAMENTE")
    return redirect(to="listar_artes")

def registro(request):
    data = {
        'form':CustomUserCreationForm
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            User = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,User)
            messages.success(request,"REGISTRADO CORRECTAMENTE")
            return redirect(to=home)
        data["form"]
    return render(request,'registration/registro.html',data)

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_artes(request):
    if request.method == 'GET':
        arte = Arte.objects.all()
        serializer = ArteSerializer(arte,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status==status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_arte(request,id):
    try:
        arte= Arte.objects.get(idprod=id)
    except Arte.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArteSerializer(arte)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArteSerializer(arte,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        arte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_artes(request):
    if request.method == 'GET':
        arte = Arte.objects.all()
        serializer = ArteSerializer(arte,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status==status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_arte(request,id):
    try:
        arte= Arte.objects.get(idprod=id)
    except Arte.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArteSerializer(arte)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArteSerializer(arte,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        arte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)