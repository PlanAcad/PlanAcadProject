# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from django.urls import reverse
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelBibliografia import Bibliografia
from planificaciones.formularios.formBibliografia import BibliografiaForm
#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
from planificaciones.funcionesDeVistas import viewCorreccion
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import pandas as pd
from django.views.decorators.csrf import csrf_exempt

@login_required
# To show and to add new one
def IndexBibliografia(request, id_planificacion):   
    planificacion = Planificacion.objects.get(id=id_planificacion)  
    bibliografias = Bibliografia.objects.filter(planificacion=planificacion)  
    mensaje_exito = None
    mensaje_error = None
   #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 9)).prefetch_related('comentarios')
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"

    
    if request.method == 'POST':
        form = BibliografiaForm(request.POST)
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                    
                mensaje_exito="Añadimos la bibliografía correctamente."  
                 
            except:  
                 mensaje_error = "No pudimos añadir la bibliografía." 

        else:
            mensaje_error = "No pudimos añadir la bibliografía." 
    form = BibliografiaForm()
    context = {
        'planificacion': planificacion,
        'bibliografias': bibliografias,
        "form": form,
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        'correccionesEnSecciones':correccionesEnSecciones,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }
    return render(request,"secciones/bibliografia/index.html", context) 



@login_required
@csrf_exempt
def ReadBibliografiaFromFile(request):
    file_excel = request.FILES.get('excel_file')
    print(file_excel)
    # Leer el archivo Excel y convertirlo en un DataFrame
    df = pd.read_excel(file_excel,engine='openpyxl')
    # Iterar sobre cada fila del DataFrame y crear usuarios de Django
    bibliografiaToAdd = []
    for _, row in df.iterrows():
        titulo = row['titulo_libro']
        if not pd.isna(titulo):
            libro = Bibliografia()
            libro.autor = row['autor']
            libro.titulo_libro = row['titulo_libro']
            libro.editor = row['editor']
            libro.año_publicacion = row['año_publicacion']
            bibliografiaToAdd.append(libro)
    
    return render(request, 'secciones/bibliografia/bibliografia-dropdown.html', {'bibliografiaToAdd': bibliografiaToAdd})

@login_required
@csrf_exempt
def AddBibliografiaFromFile(request):
    if request.method == 'POST':
        file_excel = request.FILES.get('excel_file')
        libro = request.POST.get('titulo_libro')
        planificacion_id = request.POST.get('planificacion_id')
        planificacion = Planificacion.objects.get(id=planificacion_id)
        # Leer el archivo Excel y convertirlo en un DataFrame
        df = pd.read_excel(file_excel,engine='openpyxl')
        df['año_publicacion'] = pd.to_numeric(df['año_publicacion'], errors='coerce').fillna(0).astype(int)
        # Iterar sobre cada fila del DataFrame y crear usuarios de Django
        for _, row in df.iterrows():
            titulo = row['titulo_libro']
            if not pd.isna(titulo):
                if(titulo == libro):
                    libro = Bibliografia()
                    libro.autor = row['autor']
                    libro.titulo_libro = row['titulo_libro']
                    libro.editor = row['editor']
                    libro.año_publicacion = row['año_publicacion']
                    libro.planificacion = planificacion
                    libro.save()
                    
        redirect_url = reverse('planificaciones:bibliografia', kwargs={'id_planificacion': planificacion.id})
        response = HttpResponse(redirect_url)
        return response



# To show and to add new one
@login_required
def UpdateBibliografia(request, id_planificacion, id_bibliografia):   
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    bibliografia = Bibliografia.objects.get(id=id_bibliografia)  
    form = BibliografiaForm(instance=bibliografia)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':
        form = BibliografiaForm(request.POST, instance=bibliografia)  
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                mensaje_exito="Añadimos la bibliografía correctamente." 

                return redirect('planificaciones:bibliografia', id_planificacion=id_planificacion)

                 
            except:  
                 mensaje_error = "No pudimos añadir la bibliografía." 

        else:
            mensaje_error = "No pudimos añadir la bibliografía." 
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    context = {
        'planificacion': planificacion,
        'bibliografia': bibliografia,
        "form": form,
        'correccionesEnSecciones':correccionesEnSecciones,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/bibliografia/update.html", context) 


@login_required
def Deletebibliografia(request, id_planificacion, id_bibliografia):
    mensaje_exito = None
    mensaje_error = None

    if request.method == "POST":
        try:
            bibliografia = Bibliografia.objects.get(id=id_bibliografia)  
            bibliografia.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:bibliografia', id_planificacion=id_planificacion)