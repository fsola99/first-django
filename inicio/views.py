from django.shortcuts import render
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
    paleta = Paleta(marca='wilson',descripcion='es una paleta wilson re copada',anio=1999)
    paleta.save()
    
    return render(request, 'inicio/paletas.html',{paleta:paletas})

def crear_paleta(request):
    
    # VERSION HTML
    
    # if request.mehtod == 'POST':
    #     marca = request.POST.get('marca')
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get(anio)
        
    #     paleta = Paleta(marca=marca,descripcion=descripcion,anio=anio)
    #     paleta.save()
    
    # VERSION DJANGO FORMS
    if request.method == 'POST':
        ...

    formulario = CrearPaletaFormulario()
    return render(request, 'inicio/crear_paleta.html', {'formulario': formulario})