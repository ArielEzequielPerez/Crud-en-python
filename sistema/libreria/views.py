from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Libro
from .formulario import LibroFormulario

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')
    
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html',{'libros': libros})

def crearLibros(request):
    formulario = LibroFormulario(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editarLibros(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroFormulario(request.POST or None, request.FILES or None, instance=libro)
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminarLibro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')

