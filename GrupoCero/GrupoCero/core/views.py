from django.shortcuts import render,redirect,get_object_or_404
from .models import Arte
from .forms import ContactoForm,ArteForm,CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required,permission_required
from rest_framework import viewsets
from .serializers import ArteSerializer


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

def main_esculturas(request):
    return render (request,'app/main_esculturas.html')

def main_orfebreria(request):
    return render (request,'app/main_orfebreria.html')
    
def escultura1(request):
    return render (request,'app/esculturashtmls/escultura1.html')

def escultura2(request):
    return render (request,'app/esculturashtmls/escultura2.html')


@permission_required('core.add_arte')
@login_required
def agregar_arte(request):
    data = {
        'form':ArteForm()
    }
    if request.method == 'POST':
        formulario = ArteForm(data=request.POST, files=request.FILES)
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
        formulario=ArteForm(data=request.POST, instance=arte,files=request.FILES)
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