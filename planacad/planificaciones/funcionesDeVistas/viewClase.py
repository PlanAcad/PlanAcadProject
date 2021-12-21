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

##Define request for Resultado de Aprendizaje   
def ClaseNew(request,id_planificacion): 
    mensaje_exito=None
    mensaje_error=None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = Clase.objects.filter(planificacion=planificacion)
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
        form = ClaseForm()
        form.fields['profesor_a_cargo'].queryset = Profesor.objects.filter(asignatura__id = planificacion.asignatura_id)
        form.fields['unidad_tematica_o_tema'].queryset = Contenido.objects.filter(planificacion = planificacion)
        form.fields['resultado_de_aprendizaje'].queryset = ResultadoDeAprendizaje.objects.filter(planificacion = planificacion)
         
    return render(request,'secciones/cronograma/index.html',{'planificacion':planificacion,'data':data,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
def ClasesView(request,planificacion_id):
    mensaje_error = None
    try:
         #Obtengo la planificacion
         planificacion = Planificacion.objects.get(id=planificacion_id)
         #Obtengo los resultados de aprendizaje
         clases = Clase.objects.filter(planificacion=planificacion)
         datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
         existe_calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo = datosDescriptivos.ciclo_lectivo).exists()
         cronograma_sintonizado = planificacion.sincronizado_calendario_academico
    except:
         mensaje_error = "No pudimos obtener los datos correctamente"    
    return render(request,"secciones/cronograma/.html",{'clases':clases, 'mensaje_error': mensaje_error,'existe_calendario':existe_calendario,
    'cronograma_sintonizado':cronograma_sintonizado})  
def ClaseViewDetail(request,clase_id): 
    mensaje_error = None 
    try:
         #Obtengo la clase
         clase = Clase.objects.get(id=clase_id)
    except:
         mensaje_error = "No pudimos obtener los datos correctamente" 
    return render(request,'secciones/cronograma/.html', {'clase':clase, 'mensaje_error': mensaje_error})  
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

def CronogramaCreate(request,planificacion_id):
    mensaje_error = None
    try:
         #Obtengo la planificacion
         planificacion = Planificacion.objects.get(id=planificacion_id)
         datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
         cronograma = FechaCalendarioAcademico.objects.filter(ciclo_lectivo = datosDescriptivos.ciclo_lectivo)
         form = CronogramaCreateForm(request.POST)
         dias = request.POST.get('dias')
         print(dias)
         inicio = None
         fin = None
         if (datosDescriptivos.cursado_posible=='A'):
            inicio= cronograma.get(actividad='IC1')
            fin= cronograma.get(actividad='FC2')
         elif (datosDescriptivos.cursado_posible=='1'):
            inicio= cronograma.get(actividad='IC1')
            fin= cronograma.get(actividad='FC1')
         elif (datosDescriptivos.cursado_posible=='2'):
            inicio= cronograma.get(actividad='IC2')
            fin= cronograma.get(actividad='FC2')
         cronograma = cronograma.filter(fecha__range=[inicio,fin])
         dias_cronograma = []
         if(dias.__contains__('L')):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Monday").filter(hay_clase=True))
         if (dias.__contains__('M')):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Tuesday").filter(hay_clase=True))
         if (dias.__contains__('MI')):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Wednesday").filter(hay_clase=True))
         if (dias.__contains__('J')):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Thursday").filter(hay_clase=True))
         if (dias.__contains__('V')):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Friday").filter(hay_clase=True))
         if (dias.__contains__('S')):
             dias_cronograma.extend(cronograma.filter(nombre_dia="Saturday").filter(hay_clase=True))
         try:  
            for i in dias_cronograma:  
                instance = ClaseForm()
                instance.planificacion_id=planificacion.id
                instance.save()
            planificacion.sincronizado_calendario_academico = True
            planificacion.save()
            mensaje_exito="Añadimos la clase correctamente."
         except:  
            mensaje_error = "No pudimos guardar los cambios."
    except:
         mensaje_error = "No pudimos obtener los datos correctamente"    
    return render(request,"secciones/cronograma/.html",{'mensaje_error': mensaje_error})  
