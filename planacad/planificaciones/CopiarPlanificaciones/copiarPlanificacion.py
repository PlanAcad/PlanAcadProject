from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from planificaciones.modelos.modelFundamentacion import Fundamentacion
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior
from planificaciones.modelos.modelSubCompetencia import SubCompetencia, Competencia
from planificaciones.modelos.modelPropuestaDesarrollo import PropuestaDesarrollo
from planificaciones.modelos.modelActividad import Actividad
from planificaciones.modelos.modelClase import Clase
from planificaciones.modelos.modelBibliografia import Bibliografia
from planificaciones.modelos.modelWebgrafia import Webgrafia
from planificaciones.modelos.modelFechaCalendarioAcademico import FechaCalendarioAcademico
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.modelos.modelUnidad import Unidad
from django.contrib.auth.models import User


from planificaciones.validaciones import validacionSecciones
from planificaciones.modelos.modelAsignatura import Asignatura
from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse

def CopiarIndex(request,id_planificacion):
    validacion_ok= validacionSecciones.CamposCompletos(id_planificacion)
    if(validacion_ok):
        planificacion = Planificacion.objects.get(id=id_planificacion)
        if request.method == "POST":       
            #Seccion 7.1, 7.2 ,  13 --Hecho
            planificacion.pk = None
            planificacion._state.adding = True
            datosDescriptivosId = planificacion.datos_descriptivos_id
            fundamentacionId = planificacion.fundamentacion_id
            planificacion.datos_descriptivos =None
            planificacion.fundamentacion = None
            planificacion.estado = "P"
            planificacion.save()
            print("Seccion 7.1 - 7.2- 13")
            #Seccion 1 --Hecho
            datosDescriptivos = DatosDescriptivos.objects.get(id=datosDescriptivosId)
            diasClase = datosDescriptivos.dias.all()
            datosDescriptivos.ciclo_lectivo =  datosDescriptivos.ciclo_lectivo+1
            datosDescriptivos.pk = None
            datosDescriptivos._state.adding = True
            datosDescriptivos.save()
            for dc in diasClase:
                datosDescriptivos.dias.add(dc)
            datosDescriptivos.save()
            planificacion.datos_descriptivos = datosDescriptivos
            planificacion.save()
            print("Seccion 1")
            ##Save planificacion
            #Seccion 2 -Hecho, 12 
            detallesProfesorCatedra = DetalleProfesorCatedra.objects.filter(planificacion_id=id_planificacion)
            tareasFunciones = TareasFunciones.objects.filter(planificacion_id = id_planificacion)
            for item in tareasFunciones:
                item.planificacion = planificacion
                item.pk = None
                item._state.adding = True
                item.save()

            for item in detallesProfesorCatedra:
                tareas = item.tareas.all()
                ##Copy obj    
                item.planificacion = planificacion
                item.pk = None
                item._state.adding = True
                item.save()
                ##save many to many
                for tarea in tareas:
                    new_tarea = TareasFunciones.objects.get(tarea_funcion=tarea.tarea_funcion, planificacion = planificacion)
                    item.tareas.add(new_tarea)
                   
                item.save()
            print("Seccion 2")
            #Seccion 3 --Hecho
            fundamentacion = Fundamentacion.objects.get(id=fundamentacionId)
            fundamentacion.pk = None
            fundamentacion._state.adding = True
            fundamentacion.save()
            planificacion.fundamentacion = fundamentacion
            print("Seccion 3")
            ##Save planificacion
            planificacion.save()
            #Seccion 4 --Hecho
            resultadosAnteriores = ResultadoDeAprendizajeAnterior.objects.filter(planificacion_id=id_planificacion)
            for item in resultadosAnteriores:
                item.pk = None
                item._state.adding = True
                item.planificacion = planificacion
                item.save()
            print("Seccion 4")
            #Seccion 5 --Hecho
            competencias = Competencia.objects.filter(planificacion_id=id_planificacion)
            for item in competencias:
                subcompetencias = item.subcompetencia_set.all()
                ##Copy obj 
                item.pk = None
                item._state.adding = True
                item.planificacion = planificacion
                item.save()
                for subcompetencia in subcompetencias: 
                    subcompetencia.pk = None
                    subcompetencia._state.adding = True
                    subcompetencia.competencia = Competencia.objects.get(id=item.id)
                    subcompetencia.save()
            print("Seccion 5")
            #Seccion 9 --Hecho
            bibliografias = Bibliografia.objects.filter(planificacion_id=id_planificacion)
            for item in bibliografias:
                item.pk = None
                item._state.adding = True
                item.planificacion = planificacion
                item.save()
            bibliografias = Bibliografia.objects.filter(planificacion_id=planificacion.id)
            print("Seccion 9")
            #Seccion 11 --Hecho
            contenidos = Contenido.objects.filter(planificacion_id=id_planificacion)
            for item in contenidos:
                unidad = Unidad.objects.get(id = item.unidad.id)
                unidad.pk = None
                unidad._state.adding = True
                unidad.planificacion = planificacion
                unidad.save()

                item.pk = None
                item._state.adding = True
                item.planificacion = planificacion
                item.unidad = unidad
                item.save()
            print("Seccion 11")
            #Seccion 6 --Hecho
            propuestasDeDesarrollo = PropuestaDesarrollo.objects.filter(planificacion_id=id_planificacion)
            ##Get resultados
            resultadosDeAprendizaje = ResultadoDeAprendizaje.objects.filter(planificacion_id=id_planificacion)
            ##Copy Resultados
            for ra in resultadosDeAprendizaje: 
                ra.pk = None
                ra._state.adding = True
                ra.planificacion = planificacion
                ra.save()
            resultadosDeAprendizaje = ResultadoDeAprendizaje.objects.filter(planificacion_id=planificacion.id)
            ##Copy propuestas
            for item in propuestasDeDesarrollo:
                ##Resguard 
                resultadosDeAprendizajePropuesta = item.resultados_de_aprendizaje.all()
                bibliografiasPropuesta = item.bibliografias.all()
                subcompetencias = item.subcompetencias.all()
                unidadesPropuesta = item.unidades.all()
                estrategiasDeEnseñanza = item.estrategias_ens.all()
                ##Copy obj 
                
                item.pk = None
                item._state.adding = True
                item.planificacion = planificacion
                item.save()
                ## Save bibliografias
                for bp in bibliografiasPropuesta:
                    biblioRa = Bibliografia.objects.get(planificacion_id=planificacion.id,autor = bp.autor , titulo_libro = bp.titulo_libro , nombre_capitulo = bp.nombre_capitulo)
                    item.bibliografias.add(biblioRa)
                item.save()
                ##Save bibliografias
                for s in subcompetencias:
                    comp = Competencia.objects.get(planificacion = planificacion, descripcion = s.competencia.descripcion)
                    subcomp = SubCompetencia.objects.get(competencia = comp, descripcion = s.descripcion)
                    item.subcompetencias.add(subcomp)
                item.save()
                ##Save unidades
                for u in unidadesPropuesta: 
                    uni = Unidad.objects.get(planificacion_id = planificacion.id, titulo = u.titulo)
                    item.unidades.add(uni)
                item.save()
                ##Save estrategias
                for e in estrategiasDeEnseñanza: 
                    item.estrategias_ens.add(e)
                item.save()
                ##Save resultado de aprendizaje
                for ra in resultadosDeAprendizajePropuesta:
                    result = ResultadoDeAprendizaje.objects.get(planificacion_id = planificacion.id, resultado = ra.resultado)
                    item.resultados_de_aprendizaje.add(result)
                item.save()
            print("Seccion 6")
            #Seccion 7 --Hecho
            actividades = Actividad.objects.filter(planificacion_id=id_planificacion)
            for item in actividades:
                ##Resguard resultado de aprendizaje
                resultadosDeAprendizajeActividad = item.resultados_de_aprendizaje.all()
                unidadesActividad = item.unidad_tematica.all()

                item.pk = None
                item._state.adding = True
                item.planificacion = planificacion
                item.save()
                ##Save resultado de aprendizaje
                for ra in resultadosDeAprendizajeActividad:
                    result = ResultadoDeAprendizaje.objects.get(planificacion_id = planificacion.id, resultado = ra.resultado)
                    item.resultados_de_aprendizaje.add(result)
                for u in unidadesActividad: 
                    uni = Unidad.objects.get(planificacion_id = planificacion.id, titulo = u.titulo)
                    item.unidad_tematica.add(uni)
                item.save()
            print("Seccion 7")
            #Seccion 10 --Hecho
            webgrafias = Webgrafia.objects.filter(planificacion_id=id_planificacion)
            for item in webgrafias:
                item.pk = None
                item._state.adding = True
                item.planificacion = planificacion
                item.save()
            print("Seccion 10")
            #Seccion 8 --Hecho
            ## Crear cronograma
            datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
            cronograma = FechaCalendarioAcademico.objects.filter(ciclo_lectivo = datetime.now().year)
            dias = datosDescriptivos.dias.all()
            inicio = None
            fin = None
            if (datosDescriptivos.cursado=='A'):
                inicio= cronograma.get(actividad='IC1')
                fin= cronograma.get(actividad='FC2')
            elif (datosDescriptivos.cursado=='1'):
                inicio= cronograma.get(actividad='IC1')
                fin= cronograma.get(actividad='FC1')
            elif (datosDescriptivos.cursado=='2'):
                inicio= cronograma.get(actividad='IC2')
                fin= cronograma.get(actividad='FC2')
            cronograma = cronograma.filter(fecha__range=[inicio.fecha,fin.fecha])
            dias_cronograma = []
            for d in dias:
                if(d.id ==1):
                    dias_cronograma.extend(cronograma.filter(nombre_dia="Monday").filter(hay_clase=True))
                if (d.id ==2):
                    dias_cronograma.extend(cronograma.filter(nombre_dia="Tuesday").filter(hay_clase=True))
                if (d.id ==3):
                    dias_cronograma.extend(cronograma.filter(nombre_dia="Wednesday").filter(hay_clase=True))
                if (d.id ==4):
                    dias_cronograma.extend(cronograma.filter(nombre_dia="Thursday").filter(hay_clase=True))
                if (d.id ==5):
                    dias_cronograma.extend(cronograma.filter(nombre_dia="Friday").filter(hay_clase=True))
                if (d.id ==6):
                    dias_cronograma.extend(cronograma.filter(nombre_dia="Saturday").filter(hay_clase=True))
            for i in dias_cronograma:
                instance = Clase()
                instance.planificacion_id=planificacion.id
                instance.fecha_clase=i.fecha
                instance.save()
            planificacion.sincronizado_calendario_academico = True
            planificacion.save()
            ##End create cronograma
            clasesNuevas = Clase.objects.filter(planificacion_id=planificacion.id).order_by('fecha_clase')
            clases = Clase.objects.filter(planificacion_id=id_planificacion).order_by('fecha_clase')
            i = 0
            for item in clasesNuevas:
                ##Resguard 
                if(not i >= len(clases)):
                    contenidos = clases[i].unidad_tematica_o_tema.all()
                    resultadosDeAprendizajeClase = clases[i].resultado_de_aprendizaje.all()
                    profesoresACargo = clases[i].profesor_a_cargo.all()
                    item.lugar_desarrollo_de_clase = clases[i].lugar_desarrollo_de_clase
                    item.es_examen = clases[i].es_examen
                    item.numero_de_clase_o_semana = i+1
                    item.cantidad_tareas = clases[i].cantidad_tareas
                
                    ##Save contenido
                    for c in contenidos:
                        cont = Contenido.objects.get(planificacion_id = planificacion.id, contenido = c.contenido)
                        item.unidad_tematica_o_tema.add(cont)
                    ##Save resultado de aprendizaje
                    for ra in resultadosDeAprendizajeClase:
                        result = ResultadoDeAprendizaje.objects.get(planificacion_id = planificacion.id, resultado = ra.resultado)
                        item.resultado_de_aprendizaje.add(result)
                    for p in profesoresACargo:
                        profe = User.objects.get(id = p.id)
                        item.profesor_a_cargo.add(profe)
                item.save()
                i = i+1
            print("Seccion 8")
            return redirect('planificaciones:datosDescriptivos', id_planificacion=planificacion.id)
    else:
        asignatura = Planificacion.objects.get(id = id_planificacion).asignatura
        return redirect(reverse('planificaciones:asignaturaDetail', kwargs={'id' : asignatura.id, 'error': 'True'} ))
         
 