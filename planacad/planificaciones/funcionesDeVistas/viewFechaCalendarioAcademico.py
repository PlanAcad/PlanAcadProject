# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
from django.urls import reverse
import datetime
import locale
from datetime import timedelta
from django.http import HttpResponseRedirect
from planificaciones.formularios.formFechaCalendarioAcademico import FechaCalendarioAcademicoForm
from planificaciones.formularios.formFechaCalendarioAcademico import FechaCalendarioAcademico
from django.utils.translation import get_language, activate

def CalendarioAcademicoIndex(request, año):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    mensaje_exito = None
    mensaje_error = None  
    fecha = datetime.datetime(año, 3, 1)
    calendario = None
    if request.method == "POST":
        try:
            if(FechaCalendarioAcademico.objects.filter(fecha__year = año).exists()==False):
                for i in range(366): 
                    instance = FechaCalendarioAcademico()
                    instance.fecha = fecha
                    instance.editable = True
                    instance.actividad = 'DN'
                    instance.nombre_mes = fecha.strftime('%B')
                    instance.nombre_dia = fecha.strftime('%A')
                    if(instance.nombre_dia=="domingo" or fecha.strftime('%A').startswith("s") ):
                        instance.hay_clase= False
                    else: 
                        instance.hay_clase= True
                    
                    instance.save()
                    fecha = fecha + timedelta(days=1)
                mensaje_exito="Se cargo el calendario correctamente"
            else:
                mensaje_error="ya hay un calendario con esa fecha"
            calendario =FechaCalendarioAcademico.objects.filter(fecha__year = año)                 
        except:  
            mensaje_error="no se cargo nada de nada"  
    else:  
        calendario = FechaCalendarioAcademico.objects.filter(fecha__year = año) 
    return render(request,'calendario/calendario-academico.html',{'calendario':calendario,'año':año,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito}) 


    
def UpdateFechaCalendarioAcademico(request, year_fecha_desde,month_fecha_desde,day_fecha_desde,year_fecha_hasta,month_fecha_hasta,day_fecha_hasta,actividad):  
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    mensaje_exito = None
    mensaje_error = None
    fecha_desde = datetime.datetime(year_fecha_desde, month_fecha_desde, day_fecha_desde)
    fecha_hasta= datetime.datetime(year_fecha_hasta, month_fecha_hasta, day_fecha_hasta)
    data = FechaCalendarioAcademico.objects.filter(fecha__range=[fecha_desde,fecha_hasta])
    if request.method == "POST":
        try:  
            for i in data:  
                instance = i
                instance.actividad = actividad
                if(actividad == 'EF' or actividad == 'F' or actividad == 'RI'):
                    instance.hay_clase=False
                instance.save()
            mensaje_exito="Guardamos los cambios correctamente."
        except:  
            mensaje_error = "No pudimos guardar los cambios."  
    
    context = {
        'data':data, 
        'mensaje_error': mensaje_error,
        'mensaje_exito':mensaje_exito,
        'year_fecha_desde':year_fecha_desde,
        'month_fecha_desde':month_fecha_desde,
        'day_fecha_desde':day_fecha_desde,
        'year_fecha_hasta':year_fecha_hasta,
        'month_fecha_hasta':month_fecha_hasta,
        'day_fecha_hasta':day_fecha_hasta,
        'actividad':actividad
    }

    return render(request,'calendario/calendario-academico-edit.html', context)

def CerrarCalendarioAcademico(request, año):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    mensaje_exito = None
    mensaje_error = None  
    calendario = None
    if request.method == "POST":
        try:
            if(FechaCalendarioAcademico.objects.filter(fecha__year = año).exists()):
                calendario = FechaCalendarioAcademico.objects.filter(fecha__year = año)
                for i in calendario:
                        instance = i
                        instance.editable = False
                        instance.save()
                mensaje_exito="Se cargo el calendario correctamente"
                return render(request,'calendario/calendario-academico.html',{'calendario':calendario,'año':año,'mensaje_error': mensaje_error,
'mensaje_exito':mensaje_exito}) 
            else:
                mensaje_error="ya hay un calendario con esa fecha"                
        except:  
            mensaje_error="no se cargo nada de nada"  
    else:  
        calendario = FechaCalendarioAcademico.objects.filter(fecha__year = año) 
    return render(request,'calendario/calendario-academico-cerrar.html',{'calendario':calendario,'año':año,'mensaje_error': mensaje_error,
'mensaje_exito':mensaje_exito}) 
