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
            for i in range(366): 
                instance = FechaCalendarioAcademico()
                instance.fecha = fecha
                instance.hay_clase= True
                instance.actividad = 'DN'
                instance.nombre_mes = fecha.strftime('%B')
                instance.nombre_dia = fecha.strftime('%A')
                instance.save()
                fecha = fecha + timedelta(days=1)
                print(fecha)
                print(fecha.strftime('%B'))
            calendario =FechaCalendarioAcademico.objects.filter(fecha__year = año) 
            mensaje_exito="Se cargo el calendario correctamente"  
        except:  
            mensaje_error="no se cargo nada de nada"  
    else:  
        calendario = FechaCalendarioAcademico.objects.filter(fecha__year = año) 
    return render(request,'calendario/calendario-academico.html',{'calendario':calendario,'año':año,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito}) 
