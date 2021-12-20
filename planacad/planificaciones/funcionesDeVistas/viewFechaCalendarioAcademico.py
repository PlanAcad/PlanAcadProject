# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
from django.urls import reverse
import datetime
import locale
from datetime import timedelta
from django.http import HttpResponseRedirect
from planificaciones.formularios.formFechaCalendarioAcademico import FechaCalendarioAcademicoForm
from planificaciones.formularios.formFechaCalendarioUpdate import FechaCalendarioAcademicoUpdateForm

from planificaciones.formularios.formFechaCalendarioAcademico import FechaCalendarioAcademico
from django.utils.translation import get_language, activate

def CalendarioAcademicoIndex(request, ano):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    mensaje_exito = None
    mensaje_error = None  
    fecha = datetime.datetime(ano, 3, 1)
    calendario = None
    existe_calendario = None
    if request.method == "POST":
        try:
            if(FechaCalendarioAcademico.objects.filter(fecha__year = ano).exists()==False):
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
            calendario =FechaCalendarioAcademico.objects.filter(fecha__year = ano).exclude(actividad='DN').order_by('fecha')                 
        except:  
            mensaje_error="no se cargo nada de nada"  
    else:  
        form = FechaCalendarioAcademicoUpdateForm()
        calendario = FechaCalendarioAcademico.objects.filter(fecha__year = ano).exclude(actividad='DN').order_by('fecha')
    existe_calendario = FechaCalendarioAcademico.objects.filter(fecha__year = ano).exists()  
    return render(request,'calendario/calendario-academico.html',{'calendario':calendario,'existe_calendario':existe_calendario,'ano':ano,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito, 'form':form}) 


    
def UpdateFechaCalendarioAcademico(request,ano):  
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    mensaje_exito = None
    mensaje_error = None
    form = FechaCalendarioAcademicoUpdateForm(request.POST)
    fecha_desde = request.POST.get('fecha_desde')
    fecha_desde = datetime.datetime.strptime(fecha_desde, '%d/%m/%Y')
    fecha_hasta= request.POST.get('fecha_hasta')
    if fecha_hasta == '':
        fecha_hasta = fecha_desde
    else:
        fecha_hasta = datetime.datetime.strptime(fecha_hasta, '%d/%m/%Y')
    actividad = request.POST.get('actividad')
    data = FechaCalendarioAcademico.objects.filter(fecha__range=[fecha_desde,fecha_hasta])
    if request.method == "POST":
        try:  
            for i in data:  
                instance = i
                instance.actividad = actividad
                instance.descripcion = request.POST.get('descripcion')
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
        'form':form,
        'actividad':actividad
    }

    return redirect('planificaciones:calendarioacademico', ano=ano)

def CerrarCalendarioAcademico(request, ano):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    mensaje_exito = None
    mensaje_error = None  
    calendario = None
    if request.method == "POST":
        try:
            if(FechaCalendarioAcademico.objects.filter(fecha__year = ano).exists()):
                calendario = FechaCalendarioAcademico.objects.filter(fecha__year = ano)
                for i in calendario:
                        instance = i
                        instance.editable = False
                        instance.save()
                mensaje_exito="Se cargo el calendario correctamente"
                return render(request,'calendario/calendario-academico.html',{'calendario':calendario,'año':ano,'mensaje_error': mensaje_error,
'mensaje_exito':mensaje_exito}) 
            else:
                mensaje_error="ya hay un calendario con esa fecha"                
        except:  
            mensaje_error="no se cargo nada de nada"  
    else:  
        calendario = FechaCalendarioAcademico.objects.filter(fecha__year = ano).exclude(actividad='DN').order_by('fecha')
    return render(request,'calendario/calendario-academico-cerrar.html',{'calendario':calendario,'año':ano,'mensaje_error': mensaje_error,
'mensaje_exito':mensaje_exito}) 
