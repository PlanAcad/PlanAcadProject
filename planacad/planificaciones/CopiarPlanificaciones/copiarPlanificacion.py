from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
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
from django.shortcuts import render, redirect

def CopiarIndex(request,id_planificacion):
    validacion_ok=False
    validacion_bad =False
    errores = []
    planificacion = Planificacion.objects.get(id=id_planificacion)
    if request.method == "POST":       
        #Seccion 7.1, 7.2 ,  13 --Hecho
        planificacion.pk = None
        planificacion._state.adding = True
        datosDescriptivosId = planificacion.datos_descriptivos_id
        fundamentacionId = planificacion.fundamentacion_id
        planificacion.datos_descriptivos =None
        planificacion.fundamentacion = None
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
        for item in detallesProfesorCatedra:
            ##Resguard many to many
            tareas = item.tareas.all()
            ##Copy obj    
            item.planificacion = planificacion
            item.pk = None
            item._state.adding = True
            item.save()
            ##save many to many
            for tarea in tareas:
                item.tareas.add(tarea)
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
            ##Resguard many to many
            subcompetencias = item.subcompetencia_set.all()
             ##Copy obj 
            item.pk = None
            item._state.adding = True
            item.planificacion = planificacion
            item.save()
            for subcompetencia in subcompetencias: 
                subcompetencia.pk = None
                subcompetencia._state.adding = True
                subcompetencia.competencia = item
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
        ##Copy propuestas
        for item in propuestasDeDesarrollo:
            ##Resguard 
            subcompetencias = item.subcompetencias.all()
            ##Resguard 
            unidades = item.unidades.all()
            ##Resguard 
            estrategias_ens = item.estrategias_ens.all()
            ##Resguard resultado de aprendizaje
            resultadosDeAprendizajePropuesta = item.resultados_de_aprendizaje.all()
            ## Get new resultados 
            resultadosNuevosDeAprendizajePropuesta = []
            for rap in resultadosDeAprendizajePropuesta:
                for ra in resultadosDeAprendizaje:
                    if(ra.resultado == rap.resultado):
                        resultadosNuevosDeAprendizajePropuesta.append(ra)
            ##Resguard bibliografias
            bibliografiasPropuesta = item.bibliografias.all()
            ## Get new bibliografia 
            bibliografiasNuevosDeAprendizajePropuesta = []
            for bp in bibliografiasPropuesta:
                for b in bibliografias:
                    if(bp.autor == b.autor and bp.titulo_libro == b.titulo_libro and bp.nombre_capitulo == b.nombre_capitulo):
                        bibliografiasNuevosDeAprendizajePropuesta.append(bp)
            ##Copy obj 
            item.pk = None
            item._state.adding = True
            item.planificacion = planificacion
            item.save()
            ##Save bibliografias
            for s in subcompetencias: 
                item.subcompetencias.add(s)
            item.save()
            ##Save unidades
            for u in unidades: 
                item.unidades.add(u)
            item.save()
            ##Save bibliografias
            for e in estrategias_ens: 
                item.estrategias_ens.add(e)
            item.save()
            ##Save resultado de aprendizaje
            for ra in resultadosNuevosDeAprendizajePropuesta: 
                item.resultados_de_aprendizaje.add(ra)
            item.save()
            ##Save bibliografias
            for ra in bibliografiasNuevosDeAprendizajePropuesta: 
                item.bibliografias.add(ra)
            item.save()
        print("Seccion 6")
        #Seccion 7 --Hecho
        actividades = Actividad.objects.filter(planificacion_id=id_planificacion)
        for item in actividades:
            ##Resguard resultado de aprendizaje
            resultadosDeAprendizajeActividad = item.resultados_de_aprendizaje.all()
            ## Get new resultados 
            resultadosNuevosDeAprendizajeActividad = []
            for rap in resultadosDeAprendizajeActividad:
                for ra in resultadosDeAprendizaje:
                    if(ra.resultado == rap.resultado):
                        resultadosNuevosDeAprendizajeActividad.append(ra)
            item.pk = None
            item._state.adding = True
            item.planificacion = planificacion
            item.save()
            ##Save resultado de aprendizaje
            for ra in resultadosNuevosDeAprendizajeActividad:
                item.resultados_de_aprendizaje.add(ra)
            item.save()
        print("Seccion 7")
        #Seccion 11 --Hecho
        contenidos = Contenido.objects.filter(planificacion_id=id_planificacion)
        for item in contenidos:
            item.pk = None
            item._state.adding = True
            item.planificacion = planificacion
            item.save()
        print("Seccion 11")
        #Seccion 8 --Hecho
        ## Crear cronograma
        datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
        cronograma = FechaCalendarioAcademico.objects.filter(ciclo_lectivo = datosDescriptivos.ciclo_lectivo)
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
        print(planificacion.id)
        clases = Clase.objects.filter(planificacion_id=id_planificacion).order_by('fecha_clase')
        i = 0
        for item in clasesNuevas:
            ##Resguard unidades
            unidades = clases[i].unidad_tematica_o_tema.all()
            ## Get new resultados 
            unidadesNuevoClase = []
            for rap in unidades:
                for ra in contenidos:
                    if(ra.contenido == rap.contenido):
                        unidadesNuevoClase.append(ra)
            ##Resguard resultado de aprendizaje
            resultadosDeAprendizajeClase = clases[i].resultado_de_aprendizaje.all()
            ## Get new resultados 
            resultadosNuevosDeAprendizajeClase = []
            for rap in resultadosDeAprendizajeClase:
                for ra in resultadosDeAprendizaje:
                    if(ra.resultado == rap.resultado):
                        resultadosNuevosDeAprendizajeClase.append(ra)
                ##Resguard profesores a cargo
            profesoresACargo = clases[i].profesor_a_cargo.all()

            item.lugar_desarrollo_de_clase = clases[i].lugar_desarrollo_de_clase
            item.es_examen = clases[i].es_examen
            item.numero_de_clase_o_semana = i+1
            item.cantidad_tareas = clases[i].cantidad_tareas
            
            ##Save contenido
            for u in unidadesNuevoClase:
                item.unidad_tematica_o_tema.add(u)
            ##Save resultado de aprendizaje
            for ra in resultadosNuevosDeAprendizajeClase:
                item.resultado_de_aprendizaje.add(ra)
            for p in profesoresACargo:
                item.profesor_a_cargo.add(p)
            item.save()
            i = i+1
        print("Seccion 8")
        #Seccion 10 --Hecho
        webgrafias = Webgrafia.objects.filter(planificacion_id=id_planificacion)
        for item in webgrafias:
            item.pk = None
            item._state.adding = True
            item.planificacion = planificacion
            item.save()
        print("Seccion 10")
        
    return redirect('planificaciones:datosDescriptivos', id_planificacion=planificacion.id)