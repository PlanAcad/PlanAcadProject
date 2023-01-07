# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
import planificaciones
from planificaciones.modelos.modelAsignatura import Asignatura  
## import model and form
from planificaciones.modelos.modelClase import Clase
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelProfesor import Profesor
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.formularios.formClase import  ClaseForm
from planificaciones.formularios.formResultadoDeAprendizaje import  ResultadoDeAprendizaje
##Create Cronograma
from planificaciones.modelos.modelFechaCalendarioAcademico import FechaCalendarioAcademico
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.formularios.formCronogramaCreate import  CronogramaCreateForm
#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
from planificaciones.formularios.formCorreccion import CorreccionForm


##Define request for Resultado de Aprendizaje   
def ClasesView(request,id_planificacion): 
    mensaje_exito=None
    mensaje_error=None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    cronograma_sintonizado = planificacion.sincronizado_calendario_academico
    form_create = None 
    data = Clase.objects.filter(planificacion=planificacion).order_by('fecha_clase')
    datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
    existe_calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo = datosDescriptivos.ciclo_lectivo).exists()
     #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 8)).prefetch_related('comentarios')
    existen_correcciones_pendientes = None
    correccion = CorreccionForm()
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"

    if request.method == "POST":  
        form = ClaseForm(request.POST)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                form.save_m2m()
                mensaje_exito="Añadimos la clase correctamente."  
            except:  
                 mensaje_error = "No pudimos añadir la clase."    
    else:  
        try:
            form = ClaseForm()
            form.fields['profesor_a_cargo'].queryset = Profesor.objects.filter(asignatura__id = planificacion.asignatura_id)
            form.fields['unidad_tematica_o_tema'].queryset = Contenido.objects.filter(planificacion = planificacion)
            form.fields['resultado_de_aprendizaje'].queryset = ResultadoDeAprendizaje.objects.filter(planificacion = planificacion)
            form_create = CronogramaCreateForm()    
        except:
            mensaje_error = "No pudimos obtener los datos correctamente."
    #Agregar
    context = {
        'planificacion': planificacion,
        'data':data,
        'form':form,
        'form_create': form_create,
        'correcciones':correcciones,
        'correccion_form': correccion,
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        'cronograma_sintonizado':cronograma_sintonizado, 
        'existe_calendario':existe_calendario,
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error
    }  
    return render(request,'secciones/cronograma/index.html',context)  

def ClaseViewDetail(request,clase_id): 
    mensaje_error = None 
    try:
         #Obtengo la clase
         clase = Clase.objects.get(id=clase_id)
    except:
         mensaje_error = "No pudimos obtener los datos correctamente" 
    return render(request,'secciones/cronograma/index.html', {'clase':clase, 'mensaje_error': mensaje_error})  

def ClaseUpdate(request, id_planificacion, id_clase):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = Clase.objects.get(id=id_clase)
    form = ClaseForm(instance=data)
    if request.method == "POST":  
        form = ClaseForm(request.POST, instance = data)  
        if form.is_valid():  
            try: 
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                form.save_m2m()
                mensaje_exito="Guardamos los cambios correctamente."
                return redirect('planificaciones:cronograma', id_planificacion=id_planificacion)
                 
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = ClaseForm(instance=data)
        form.fields['profesor_a_cargo'].queryset = Profesor.objects.filter(asignatura__id = planificacion.asignatura_id)
        form.fields['unidad_tematica_o_tema'].queryset = Contenido.objects.filter(planificacion = planificacion)
        form.fields['resultado_de_aprendizaje'].queryset = ResultadoDeAprendizaje.objects.filter(planificacion = planificacion)  
    return render(request,'secciones/cronograma/editar.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 

def ClaseDestroy(request,id_planificacion,id_clase):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        try:
            clase = Clase.objects.get(id=id_clase)  
            clase.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:cronograma', id_planificacion=id_planificacion)

def CronogramaCreate(request,id_planificacion):
    mensaje_error = None
    try:
         #Obtengo la planificacion
         print(id_planificacion)
         planificacion = Planificacion.objects.get(id=id_planificacion)
         datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
         print(datosDescriptivos)
         print(datosDescriptivos.ciclo_lectivo)
         cronograma = FechaCalendarioAcademico.objects.filter(ciclo_lectivo = datosDescriptivos.ciclo_lectivo)
         print(cronograma)
         dias = request.POST.get('dias')
         print(dias)
         inicio = None
         fin = None
         print(datosDescriptivos.cursado)
         if (datosDescriptivos.cursado=='A'):
            inicio= cronograma.get(actividad='IC1')
            fin= cronograma.get(actividad='FC2')
         elif (datosDescriptivos.cursado=='1'):
            inicio= cronograma.get(actividad='IC1')
            fin= cronograma.get(actividad='FC1')
         elif (datosDescriptivos.cursado=='2'):
            inicio= cronograma.get(actividad='IC2')
            fin= cronograma.get(actividad='FC2')
         print(inicio)
         print(fin)
         cronograma = cronograma.filter(fecha__range=[inicio.fecha,fin.fecha])
         print(cronograma)
         dias_cronograma = []
         print(dias_cronograma)
         if('L' in dias):
             print('Lunes')
             dias_cronograma.extend(cronograma.filter(nombre_dia="Monday").filter(hay_clase=True))
         if ('M' in dias):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Tuesday").filter(hay_clase=True))
         if ('MI' in dias):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Wednesday").filter(hay_clase=True))
         if ('J' in dias):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Thursday").filter(hay_clase=True))
         if ('V' in dias):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Friday").filter(hay_clase=True))
         if ('S' in dias):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Saturday").filter(hay_clase=True))
         print(len(dias_cronograma))
         try:  
            for i in dias_cronograma:
                print("hola")  
                instance = Clase()
                instance.planificacion_id=id_planificacion
                instance.fecha_clase=i.fecha
                instance.save()
            planificacion.sincronizado_calendario_academico = True
            planificacion.save()
            mensaje_exito="Añadimos la clase correctamente."
         except:  
            mensaje_error = "No pudimos guardar los cambios."
    except:
         mensaje_error = "No pudimos obtener los datos correctamente" 
    return redirect('planificaciones:cronograma', id_planificacion=id_planificacion)
