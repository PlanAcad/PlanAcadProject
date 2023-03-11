# Para usar los objetos y/o funciones de 'redirect'  
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
from django.db.models import Q
from django.shortcuts import render, redirect
from planificaciones.modelos.modelFechaCalendarioAcademico import FechaCalendarioAcademico  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.modelos.modelCorrecciones import Correccion
from planificaciones.formularios.formDatosDescriptivos import  DatosDescriptivosForm
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
from planificaciones.funcionesDeVistas import viewCorreccion
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required
import pandas as pd


##Define request for Asignatura

def DatosDescriptivosNew(asignatura_id, carrera_id):      
        form = DatosDescriptivos()  
        # Asigno la asignatura y carrera, no hace falta ir a buscar el objeto
        form.asignatura_id = asignatura_id
        form.carrera_id = carrera_id
        # Guardo el objeto definitivamente
        form.save()
        # redirect to a new URL:
        return  form


@login_required
def ImportDatosDescriptivos(request, id_planificacion):
    if request.method == 'POST':
        planificacion = Planificacion.objects.get(id=id_planificacion)
        datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
        # Leer el archivo Excel y convertirlo en un DataFrame
        df = pd.read_excel(request.FILES['excel_file'],engine='openpyxl')
        df['nivel'] = pd.to_numeric(df['nivel'], errors='coerce').fillna(0).astype(int)
        # Iterar sobre cada fila del DataFrame y crear usuarios de Django
        for _, row in df.iterrows():
            institucion = row['institucion']
            if not pd.isna(institucion):
                datosDescriptivos.institucion = row['institucion']
                datosDescriptivos.departamento = row['departamento']
                datosDescriptivos.area_bloque = row['area_bloque']
                datosDescriptivos.porcentaje_horas_en_carrera = row['porcentaje_horas_en_carrera']
                datosDescriptivos.porcentaje_horas_en_area = row['porcentaje_horas_en_area']
                datosDescriptivos.nivel = row['nivel']
                datosDescriptivos.ciclo_lectivo = datetime.now().year
                datosDescriptivos.carga_horaria_total = row['carga_horaria_total']
                datosDescriptivos.carga_horaria_semanal = row['carga_horaria_semanal']
                datosDescriptivos.cursado = row['cursado'].strip('"')
                datosDescriptivos.save()

        
        return redirect(reverse('planificaciones:datosDescriptivos', args=[planificacion.id]) )

# Esto muestro en /seccion1
# Si es un POST actualiza
# Si es un GET mando el form y los datos actuales
@login_required
def DatosDescriptivosUpdate(request, id_planificacion):
    data = None
    errores = []  
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
    form = DatosDescriptivosForm(instance = datosDescriptivos)
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 1)).prefetch_related('comentarios')
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"
    
    mensaje_exito = None
    mensaje_error = None
    data_json = request.GET.get('data')
    if(data_json):
        data = json.loads(data_json)
    if request.method == 'POST':  
        form = DatosDescriptivosForm(request.POST,instance = datosDescriptivos)
        if form.is_valid():
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."
               
            except:
                mensaje_error = "No pudimos guardar los cambios."
    #Agregar
    context = {
        'planificacion': planificacion,
        'form': form,
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        'correccionesEnSecciones':correccionesEnSecciones,
        #
        'datosDescriptivos': datosDescriptivos,
        'existen_correcciones_pendientes': existen_correcciones_pendientes,
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error,
        'errores': data
    }

    return render(request, 'secciones/datos-descriptivos.html', context) 

## Estos de abajo no se usan
@login_required
def DatosDescriptivosView(request):  
    datosDescriptivos = DatosDescriptivos.objects.all()
    return render(request,"profesores/index.html",{'datosDescriptivos':datosDescriptivos})  

@login_required
def DatosDescriptivosDetailView(request, id):  
    datosDescriptivos = DatosDescriptivos.objects.get(id=id)
    calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')

    return render(request,'profesores/detail.html', {'datosDescriptivos':datosDescriptivos, 'calendario': calendario})  
    
@login_required
def DatosDescriptivosDestroy(request, id):  
    datosDescriptivos = DatosDescriptivos.objects.get(id=id)  
    datosDescriptivos.delete()  
    return datosDescriptivos("/show")  