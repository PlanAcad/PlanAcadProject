# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
from django.urls import reverse
import datetime
import locale
from django.db.models import Q
from datetime import timedelta
from django.http import HttpResponseRedirect
from planificaciones.formularios.formFechaCalendarioAcademico import FechaCalendarioAcademicoForm
from planificaciones.formularios.formFechaCalendarioUpdate import FechaCalendarioAcademicoUpdateForm

from planificaciones.formularios.formFechaCalendarioAcademico import FechaCalendarioAcademico
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelClase import Clase
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelUsuarioPlanificacion import PlanificacionUsuario
from django.contrib.auth.models import User, Group
from planificaciones.funcionesDeVistas import viewCalendario
import smtplib
from email.mime.text import MIMEText
from django.utils.translation import get_language, activate
from django.contrib.auth.decorators import login_required

@login_required
def CalendarioAcademicoIndex(request, ano):
    mensaje_exito = None
    mensaje_error = None  
    fecha = datetime.datetime(ano, 3, 1)
    fecha_inicio = fecha
    fecha_fin = datetime.datetime(ano+1,3,31)
    cantidad_de_dias = (fecha_fin - fecha_inicio).days 
    calendario = None
    calendarioAcademico = None
    existe_calendario = None
    fechasParciales = None
    if request.method == "POST":
        try:
            if(FechaCalendarioAcademico.objects.filter(ciclo_lectivo = ano).exists()==False):
                for i in range(cantidad_de_dias+1): 
                    instance = FechaCalendarioAcademico()
                    instance.fecha = fecha
                    instance.ciclo_lectivo = ano
                    instance.editable = True
                    instance.actividad = 'DN'
                    instance.nombre_mes = fecha.strftime('%B')
                    
                    instance.nombre_dia = fecha.strftime('%A')
                    if(instance.nombre_dia=="Saturday" or instance.nombre_dia=="Sunday" ):
                        instance.hay_clase= False
                    else: 
                        instance.hay_clase= True
                    instance.save()
                    fecha = fecha + timedelta(days=1)
                mensaje_exito="Creamos el calendario correctamente"
            else:
                mensaje_error="ya hay un calendario con esa fecha"
            calendario =FechaCalendarioAcademico.objects.filter(ciclo_lectivo = ano).exclude(actividad='DN').order_by('fecha')                 
        except:  
            mensaje_error="no se cargo nada de nada"  
    else:
         # Obtener planificaciones existentes
        usergroup = request.user.groups.values_list('name',flat = True)
        usuariosPlanificacion = PlanificacionUsuario.objects.filter(usuario_id = request.user.id)
        if "profesor" in  usergroup  :
            asignaturasProfesor = Asignatura.objects.filter(profesor = request.user)
            for asig in asignaturasProfesor:
                planificacion = Planificacion.objects.filter(asignatura = asig).filter(datos_descriptivos__ciclo_lectivo = ano , estado = 'A').last()
                if fechasParciales:
                    fechasParciales = fechasParciales | Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'P'))
                else:
                    fechasParciales =  Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'P'))
        elif "jefe de carrera" in  usergroup or "consejo" in  usergroup:
            carreraUsuario = request.user.carrera.all()
            if(carreraUsuario.count()==1):
                carrera = Carrera.objects.get(id = carreraUsuario.first().id) 
                asignaturasProfesor = Asignatura.objects.filter(carrera = carrera)
            for asig in asignaturasProfesor:
                planificacion = Planificacion.objects.filter(asignatura = asig).filter(datos_descriptivos__ciclo_lectivo = ano , estado = 'A').last()
                if fechasParciales:
                    fechasParciales = fechasParciales | Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'P'))
                else:
                    fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'P'))
        elif "alumno" in usergroup:
            for up in usuariosPlanificacion:
                planificacion = Planificacion.objects.get(id = up.planificacion_id)
                if(planificacion.datos_descriptivos.ciclo_lectivo == ano and planificacion.estado == 'A'):
                    if fechasParciales:
                        fechasParciales = fechasParciales | Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'P'))
                    else:
                        fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'P'))

        calendarioAcademico = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=ano).exclude(actividad='DN').order_by('fecha')    
    
    calendario = viewCalendario.CreateCalendario(calendarioAcademico, fechasParciales)

    
    form = FechaCalendarioAcademicoUpdateForm()
    existe_calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo = ano).exists()  
    cerrado = FechaCalendarioAcademico.objects.filter(ciclo_lectivo = ano).filter(editable = False).exists()

    context = {
            'calendarioAcademico': calendarioAcademico,
            'calendario':calendario, 
            'existe_calendario':existe_calendario,
            'ano':ano,
            'mensaje_error': mensaje_error,
            'mensaje_exito':mensaje_exito, 
            'form':form, 
            'cerrado': cerrado
        }  

    return render(request,'calendario/calendario-academico.html',context) 

@login_required
def UpdateFechaCalendarioAcademico(request,ano):  
    # locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
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
    print(actividad)
    data = FechaCalendarioAcademico.objects.filter(fecha__range=[fecha_desde,fecha_hasta])
    if request.method == "POST":
        try:  
            for i in data:  
                instance = i
                instance.actividad = actividad
                instance.descripcion = request.POST.get('descripcion')
                print(instance.actividad)
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

@login_required
def CerrarCalendarioAcademico(request, ano):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    mensaje_exito = None
    mensaje_error = None  
    calendario = None
    if request.method == "POST":
        try:
            if(FechaCalendarioAcademico.objects.filter(ciclo_lectivo = ano).exists()):
                calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo = ano)
                calendario.update(editable = False)
                mensaje_exito="Cerramos el calendario correctamente"
                
                prefesores = Group.objects.get(name='profesor')
                jefes = Group.objects.get(name='jefe de carrera')
                consejeros = Group.objects.get(name='consejo')
                

                users = User.objects.filter(Q(groups__name=prefesores.name) | Q(groups__name=jefes.name) | Q(groups__name=consejeros.name))
                ## Me conecto al servidor
                server = smtplib.SMTP('smtp-mail.outlook.com', 587)
                server.starttls()
                server.login("victoria060298@ca.frre.utn.edu.ar", "Vi02cto0$$")
                from_email = "victoria060298@ca.frre.utn.edu.ar"
                for usuario in users:
                    to_email = usuario.email
                    message = 'Calendario Academico'
                    message = MIMEText(message)
                    message["Content-Type"] = "text/plain; charset=UTF-8"
                    message['subject'] = f'Se ha cerra el calendario academico del ciclo lectivo {ano}' 
                    msg = message.as_string()
                    server.sendmail(from_email, to_email, msg)
                ##Cierro conexion al servidor
                server.quit()

                return render(request,'calendario/calendario-academico.html',{'calendario':calendario,'año':ano,'mensaje_error': mensaje_error,
                        'mensaje_exito':mensaje_exito}) 
            else:
                mensaje_error="ya hay un calendario con esa fecha"                
        except:  
            mensaje_error="no se cargo nada de nada"  
    else:  
        calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo = ano).exclude(actividad='DN').order_by('fecha')
    return redirect('planificaciones:calendarioacademico', ano=ano)
