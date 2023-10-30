from django.shortcuts import render, redirect
from .forms import CrearMancuernaFormulario, CrearMaquinaFormulario, CrearBarraFormulario

from inicio.models import Maquina, Mancuerna, Barra

def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def maquinas(request):
    maquina_a_buscar = request.GET.get("nombre")
    
    if maquina_a_buscar:
        listado_de_maquinas = Maquina.objects.filter(nombre__icontains=maquina_a_buscar)
    else:
        listado_de_maquinas = Maquina.objects.all()
    
    return render(request, 'inicio/maquinas.html', {'listado_de_maquinas':listado_de_maquinas})

def mancuernas(request):
    mancuerna_a_buscar = request.GET.get("peso")
    
    if mancuerna_a_buscar:
        listado_de_mancuernas = Mancuerna.objects.filter(peso=mancuerna_a_buscar)
    else:
        listado_de_mancuernas = Mancuerna.objects.all()
    
    return render(request, 'inicio/mancuernas.html', {'listado_de_mancuernas':listado_de_mancuernas})

def barras(request):
    barras_a_buscar = request.GET.get("tipo")
    
    if barras_a_buscar:
        listado_de_barras = Barra.objects.filter(tipo=barras_a_buscar)
    else:
        listado_de_barras = Barra.objects.all()
    
    return render(request, 'inicio/barras.html', {'listado_de_barras':listado_de_barras})

def crear_maquina(request):
    
    if request.method == 'POST':
        formulario = CrearMaquinaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            # Valores de todos los productos
            marca = info_limpia.get('marca')
            precio = info_limpia.get('precio')
            
            # Específicos Maquina
            instrucciones_de_uso = info_limpia.get('instrucciones_de_uso')
            peso_limite = info_limpia.get('peso_limite')
            nombre = info_limpia.get('nombre')
            
            maquina = Maquina(marca=marca,precio=precio,instrucciones_de_uso=instrucciones_de_uso,peso_limite=peso_limite,nombre=nombre)
            maquina.save()
            
            return redirect('maquinas')
        else:
            return render(request, 'inicio/crear_maquina.html', {'formulario': formulario})
        
    formulario = CrearMaquinaFormulario()
    return render(request, 'crear_maquina.html', {'formulario': formulario})

def crear_maquina(request):
    
    if request.method == 'POST':
        formulario = CrearMancuernaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            # Valores de todos los productos
            marca = info_limpia.get('marca')
            precio = info_limpia.get('precio')
            
            # Específicos Mancuerna
            peso = info_limpia.get('peso')
            
            mancuerna = Maquina(marca=marca,precio=precio,peso=peso)
            mancuerna.save()
            
            return redirect('mancuernas')
        else:
            return render(request, 'inicio/crear_mancuerna.html', {'formulario': formulario})
        
    formulario = CrearMancuernaFormulario()
    return render(request, 'inicio/crear_mancuerna.html', {'formulario': formulario})

def crear_barra(request):
    
    if request.method == 'POST':
        formulario = CrearBarraFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            # Valores de todos los productos
            marca = info_limpia.get('marca')
            precio = info_limpia.get('precio')
            
            # Específicos Maquina
            tipo = info_limpia.get('tipo')
            peso = info_limpia.get('peso')
            
            barra = Maquina(marca=marca,precio=precio,tipo=tipo,peso=peso)
            barra.save()
            
            return redirect('barras')
        else:
            return render(request, 'inicio/crear_barra.html', {'formulario': formulario})
        
    formulario = CrearBarraFormulario()
    return render(request, 'crear_barra.html', {'formulario': formulario})