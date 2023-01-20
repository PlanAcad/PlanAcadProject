# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formCategoria import CategoriaForm
from planificaciones.modelos.modelCategoria import Categoria
from django.contrib.auth.decorators import login_required


##Define request for Asignatura   
@login_required
def CategoriaNew(request):
    mensaje_exito = None
    mensaje_error = None  
    if request.method == "POST":  
        form = CategoriaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                mensaje_exito=""  
            except:  
                mensaje_error=""  
    else:  
        form = CategoriaForm()  
    return render(request,'index.html',{'form':form,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito}) 

@login_required
def CategoriasView(request):
    mensaje_exito = None
    mensaje_error = None
    try:
         categorias = Categoria.objects.all()  
    except:
         mensaje_error = ""  
    return render(request,"",{'categorias':categorias,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  

@login_required
def CategoriaDetailView(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         categoria = Categoria.objects.get(id=id)   
    except:
         mensaje_error = ""  
    return render(request,'', {'categoria':categoria,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  
 
@login_required
def CategoriaUpdate(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         categoria = Categoria.objects.get(id=id)  
         form = CategoriaForm(request.POST, instance = categoria)  
         if form.is_valid():  
            form.save()
            mensaje_exito=""
         else:
               mensaje_error = ""
    except:
         mensaje_error = ""   
    return render(request, 'edit.html', {'categoria': categoria,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  
@login_required
def CategoriaDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         categoria = Categoria.objects.get(id=id)  
         categoria.delete() 
         mensaje_exito = ""
    except:
         mensaje_error = ""  
    return categoria("/show",{'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  