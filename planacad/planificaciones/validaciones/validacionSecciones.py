from planificaciones.validaciones import validacionDatosDescriptivos,validacionEstructuraDeLaCatedra, validacionFundamentacion, validacionResultadoAprendizajeAnterior
from planificaciones.validaciones import validacionCompetenciasySubcompetencia, validacionPropuestaDeDesarrollo,validacionSistemaDeEvaluacion, validacionCondicionAprobacion, validacionCronograma
from planificaciones.validaciones import validarBibliografia,validacionWebgrafia, validacionContenido,validacionDistribucionDeTareas, validacionJustificacion
from planificaciones.modelos.modelPlanificacion import Planificacion
from django.shortcuts import render

def Validacion(request,id_planificacion):
    validacion_ok=False
    validacion_bad =False
    errores = []
    planificacion = Planificacion.objects.get(id=id_planificacion)
    ##
    if request.method == "POST":
        seccion1= validacionDatosDescriptivos.ValidarSeccion(id_planificacion)
        validacion_ok = seccion1[0]
        validacion_bad = seccion1[1]
        if(seccion1[1]):
            errores.append("Seccion Datos Descriptivos")
            errores.append(seccion1[2])

        
        seccion2= validacionEstructuraDeLaCatedra.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion2[0]
        validacion_bad = validacion_bad or seccion2[1]
        if(seccion2[1]):
            errores.append("Seccion Estructura de la Catedra")
            errores.append(seccion2[2])

        seccion3= validacionFundamentacion.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion3[0]
        validacion_bad = validacion_bad or seccion3[1]
        if(seccion3[1]):
            errores.append("Seccion Fundamentacion")
            errores.append(seccion3[2])
        
        seccion4= validacionResultadoAprendizajeAnterior.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion4[0]
        validacion_bad = validacion_bad or seccion4[1]
        if(seccion4[1]):
            errores.append("Seccion RA Previos")
            errores.append(seccion4[2])
        
        seccion5= validacionCompetenciasySubcompetencia.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion5[0]
        validacion_bad = validacion_bad or seccion5[1]
        if(seccion5[1]):
            errores.append("Seccion Competencias y capacidades")
            errores.append(seccion5[2])

        seccion6= validacionPropuestaDeDesarrollo.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion6[0]
        validacion_bad = validacion_bad or seccion6[1]
        if(seccion6[1]):
            errores.append("Seccion Competencias y capacidades")
            errores.append(seccion6[2])

        seccion7= validacionSistemaDeEvaluacion.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion7[0]
        validacion_bad = validacion_bad or seccion7[1]
        if(seccion7[1]):
            errores.append("Seccion Sistema de Evaluacion")
            errores.append(seccion7[2])
        
        seccion7_1_2= validacionCondicionAprobacion.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion7_1_2[0]
        validacion_bad = validacion_bad or seccion7_1_2[1]
        if(seccion7_1_2[1]):
            errores.append("Seccion Condicion aprobacion directa y de cursada")
            errores.append(seccion7_1_2[2])
        

        seccion8= validacionCronograma.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion8[0]
        validacion_bad = validacion_bad or seccion8[1]
        if(seccion8[1]):
            errores.append("Seccion Cronograma")
            errores.append(seccion8[2])
        
        

        seccion9= validarBibliografia.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion9[0]
        validacion_bad = validacion_bad or seccion9[1]
        if(seccion1[1]):
            errores.append("Seccion Bibliografia")
            errores.append(seccion9[2])

        seccion10= validacionWebgrafia.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion10[0]
        validacion_bad = validacion_bad or seccion10[1]
        if(seccion10[1]):
            errores.append("Seccion Webgrafia")
            errores.append(seccion10[2])
        
        seccion11= validacionContenido.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion11[0]
        validacion_bad = validacion_bad or seccion11[1]
        if(seccion11[1]):
            errores.append("Seccion Contenido")
            errores.append(seccion11[2])
        
        seccion12= validacionDistribucionDeTareas.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion12[0]
        validacion_bad = validacion_bad or seccion12[1]
        if(seccion12[1]):
            errores.append("Seccion Distribucion de Tareas")
            errores.append(seccion12[2])

        seccion13= validacionJustificacion.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion13[0]
        validacion_bad = validacion_bad or seccion13[1]
        if(seccion13[1]):
            errores.append("Seccion Justificacion")
            errores.append(seccion13[2])
            
def ValidacionIndex(request,id_planificacion):
    validacion_ok=False
    validacion_bad =False
    errores = []
    planificacion = Planificacion.objects.get(id=id_planificacion)
    ##
    if request.method == "POST":
        seccion1= validacionDatosDescriptivos.ValidarSeccion(id_planificacion)
        validacion_ok = seccion1[0]
        validacion_bad = seccion1[1]
        if(seccion1[1]):
            errores.append("Seccion Datos Descriptivos")
            errores.append(seccion1[2])

        
        seccion2= validacionEstructuraDeLaCatedra.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion2[0]
        validacion_bad = validacion_bad or seccion2[1]
        if(seccion2[1]):
            errores.append("Seccion Estructura de la Catedra")
            errores.append(seccion2[2])

        seccion3= validacionFundamentacion.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion3[0]
        validacion_bad = validacion_bad or seccion3[1]
        if(seccion3[1]):
            errores.append("Seccion Fundamentacion")
            errores.append(seccion3[2])
        
        seccion4= validacionResultadoAprendizajeAnterior.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion4[0]
        validacion_bad = validacion_bad or seccion4[1]
        if(seccion4[1]):
            errores.append("Seccion RA Previos")
            errores.append(seccion4[2])
        
        seccion5= validacionCompetenciasySubcompetencia.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion5[0]
        validacion_bad = validacion_bad or seccion5[1]
        if(seccion5[1]):
            errores.append("Seccion Competencias y capacidades")
            errores.append(seccion5[2])

        seccion6= validacionPropuestaDeDesarrollo.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion6[0]
        validacion_bad = validacion_bad or seccion6[1]
        if(seccion6[1]):
            errores.append("Seccion Competencias y capacidades")
            errores.append(seccion6[2])

        seccion7= validacionSistemaDeEvaluacion.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion7[0]
        validacion_bad = validacion_bad or seccion7[1]
        if(seccion7[1]):
            errores.append("Seccion Sistema de Evaluacion")
            errores.append(seccion7[2])
        
        seccion7_1_2= validacionCondicionAprobacion.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion7_1_2[0]
        validacion_bad = validacion_bad or seccion7_1_2[1]
        if(seccion7_1_2[1]):
            errores.append("Seccion Condicion aprobacion directa y de cursada")
            errores.append(seccion7_1_2[2])
        

        seccion8= validacionCronograma.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion8[0]
        validacion_bad = validacion_bad or seccion8[1]
        if(seccion8[1]):
            errores.append("Seccion Cronograma")
            errores.append(seccion8[2])
        
        

        seccion9= validarBibliografia.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion9[0]
        validacion_bad = validacion_bad or seccion9[1]
        if(seccion1[1]):
            errores.append("Seccion Bibliografia")
            errores.append(seccion9[2])

        seccion10= validacionWebgrafia.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion10[0]
        validacion_bad = validacion_bad or seccion10[1]
        if(seccion10[1]):
            errores.append("Seccion Webgrafia")
            errores.append(seccion10[2])
        
        seccion11= validacionContenido.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion11[0]
        validacion_bad = validacion_bad or seccion11[1]
        if(seccion11[1]):
            errores.append("Seccion Contenido")
            errores.append(seccion11[2])
        
        seccion12= validacionDistribucionDeTareas.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion12[0]
        validacion_bad = validacion_bad or seccion12[1]
        if(seccion12[1]):
            errores.append("Seccion Distribucion de Tareas")
            errores.append(seccion12[2])

        seccion13= validacionJustificacion.ValidarSeccion(id_planificacion)
        validacion_ok = validacion_ok and seccion13[0]
        validacion_bad = validacion_bad or seccion13[1]
        if(seccion13[1]):
            errores.append("Seccion Justificacion")
            errores.append(seccion13[2])
        
        
        
    return render(request,'secciones/validacion.html',{'validacion_ok':validacion_ok,'validacion_bad':validacion_bad,
    'errores':errores,'planificacion': planificacion}) 