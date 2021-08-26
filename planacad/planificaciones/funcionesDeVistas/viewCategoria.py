# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formCategoria import CategoriaForm
from planificaciones.modelos.modelCategoria import Categoria
##Define request for Asignatura   
def NewCategoria(request):  
    if request.method == "POST":  
        form = CategoriaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
            except:  
                pass  
    else:  
        form = CategoriaForm()  
    return render(request,'index.html',{'form':form}) 

def CategoriasView(request):  
    categorias = Categoria.objects.all()  
    return render(request,"",{'categorias':categorias})  

def CategoriaDetailView(request, id):  
    categoria = Categoria.objects.get(id=id)  
    return render(request,'', {'categoria':categoria})  
 
def CategoriaUpdate(request, id):  
    categoria = Categoria.objects.get(id=id)  
    form = CategoriaForm(request.POST, instance = categoria)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'categoria': categoria})  

def CategoriaDestroy(request, id):  
    categoria = Categoria.objects.get(id=id)  
    categoria.delete()  
    return categoria("/show")  