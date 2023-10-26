from django.shortcuts import render, redirect
from .forms import CrearPaletaFormulario

# ESTAS DOS YA QUEDARÍAN OBSOLETAS
#from django.http import HttpResponse
#from django.template import loader

from inicio.models import Paleta

def inicio(request):
    
    # V2
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})
    
    # return HttpResponse(template_renderizado)
    
    # V3 y Final.
    return render(request, 'inicio/inicio.html', {})

def paletas(request):
    marca_a_buscar = request.GET.get("marca")
    
    if marca_a_buscar:
        listado_de_paletas = Paleta.objects.filter(marca__icontains=marca_a_buscar)
    else:
        listado_de_paletas = Paleta.objects.all()
    
    
    
    
    return render(request, 'inicio/paletas.html', {'listado_de_paletas':listado_de_paletas})

def crear_paleta(request):
    
    # VERSION HTML
    
    # if request.mehtod == 'POST':
    #     marca = request.POST.get('marca')
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get('anio')
        
    #     paleta = Paleta(marca=marca,descripcion=descripcion,anio=anio)
    #     paleta.save()
    
    # VERSION DJANGO FORMS
    if request.method == 'POST':
        formulario = CrearPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            
            paleta = Paleta(marca=marca,descripcion=descripcion,anio=anio)
            paleta.save()
            
            return redirect('paletas')
        else:
            return render(request, 'inicio/crear_paleta.html', {'formulario': formulario})
        
    formulario = CrearPaletaFormulario()
    return render(request, 'inicio/crear_paleta.html', {'formulario': formulario})