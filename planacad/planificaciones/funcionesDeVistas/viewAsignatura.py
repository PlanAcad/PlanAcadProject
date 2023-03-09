from django.db.models import Q
# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.formularios.formPlanificacion import PlanificacionForm
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formAsignatura import AsignaturaForm 
from planificaciones.formularios.formAsignaturasCarrera import AsignaturaCarreraForm 
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.modelos.modelClase import Clase
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelUsuarioPlanificacion import PlanificacionUsuario
from django.contrib.auth.models import User

from planificaciones.formularios.formFechaCalendarioAcademico import FechaCalendarioAcademico
from planificaciones.funcionesDeVistas import viewCalendario
from datetime import datetime
from django.contrib.auth.decorators import login_required
import smtplib
from email.mime.text import MIMEText
import pandas as pd

@login_required
def AsignaturaNew(request):
    form = AsignaturaForm()
    if request.method == "POST":
        form = AsignaturaForm(request.POST)  
        if form.is_valid():
            print("guarda")
            asig = form.save(commit=False)
            asig.save()
            form.save_m2m()
            return redirect('planificaciones:updateAsignatura')

    context = {
        'form':form,
         
    }      
    return render(request, 'asignaturas/add.html', context)

@login_required
def bulkAsignaturaNew(request):
    if request.method == 'POST':
        # Leer el archivo Excel y convertirlo en un DataFrame
        df = pd.read_excel(request.FILES['excel_file'],engine='openpyxl')
        df['ano'] = pd.to_numeric(df['ano'], errors='coerce').fillna(0).astype(int)
        # Iterar sobre cada fila del DataFrame y crear usuarios de Django
        for _, row in df.iterrows():
            nombreCarrera = row['carrera']
            if not pd.isna(nombreCarrera):
                carrera = Carrera.objects.get(nombre_carrera = row['carrera'])
                asignatura = Asignatura.objects.create(
                    nombre_materia= row['name'],
                    ano=row['ano'],
                    comision=row['comision'],
                    carrera_id= carrera.id
                )
                for userNameProfesor in row['profesores'].split(','):
                        if(userNameProfesor):
                            prof = User.objects.get(username=userNameProfesor.strip('"'))
                            asignatura.profesor.add(prof)
                            asignatura.save()
        return redirect('planificaciones:asignaturas')

@login_required
def AsignaturasView(request):
    if(not request.user.is_staff):
        # Obtener materias del profesor
        asignaturas = None
        calendario = None
        usergroup = request.user.groups.values_list('name',flat = True)

        usuariosPlanificacion = PlanificacionUsuario.objects.filter(usuario_id = request.user.id)
        fechasParciales = None

        carrerasUsuario = request.user.carrera.all()
        if(carrerasUsuario.count()==1):
            carreraUsuario = Carrera.objects.get(id = carrerasUsuario.first().id)
        formAsignaturaCarrera = AsignaturaCarreraForm()

        if "profesor" in  usergroup  :
            asignaturas = Asignatura.objects.filter(profesor=request.user)
            for asig in asignaturas:
                planificacion = Planificacion.objects.filter(asignatura = asig).filter(datos_descriptivos__ciclo_lectivo = str(datetime.now().year) , estado = 'A').last()
                fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)
        elif "jefe de carrera" in  usergroup or "consejo" in  usergroup :
            carrerasUsuario = request.user.carrera.all()
            if(carrerasUsuario.count()==1):
                carreraUsuario = Carrera.objects.get(id = carrerasUsuario.first().id) 
                asignaturas = Asignatura.objects.filter(carrera = carreraUsuario)
            for asig in asignaturas:
                planificacion = Planificacion.objects.filter(asignatura = asig).filter(datos_descriptivos__ciclo_lectivo = str(datetime.now().year) , estado = 'A').last()
                fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)
        
        elif "alumno" in usergroup:
            carrerasUsuario = request.user.carrera.all()
            if(carrerasUsuario.count()==1):
                carreraUsuario = Carrera.objects.get(Q(id = carrerasUsuario.first().id)) 
                asignaturas = Asignatura.objects.filter(carrera = carreraUsuario) | Asignatura.objects.filter(carrera__nombre_carrera = "Basicas")
            for up in usuariosPlanificacion:
                planificacion = Planificacion.objects.get(id = up.planificacion_id)
                if(planificacion.datos_descriptivos.ciclo_lectivo == str(datetime.now().year) and planificacion.estado == 'A'):
                    fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)

        
        
        formAsignaturaCarrera.fields['asignaturas'].queryset = Asignatura.objects.filter(carrera=carreraUsuario)
        calendarioAcademico = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')    
        calendario = viewCalendario.CreateCalendario(calendarioAcademico, fechasParciales)

        if(asignaturas):
            asignaturas = asignaturas.order_by('ano')

        context = {
                'asignaturas': asignaturas,
                'calendario':calendario, 
                'formAsignaturaCarrera':formAsignaturaCarrera
            }  
        return render(request,'asignaturas/index.html', context)
    else:
        asignaturasISI = None
        asignaturasIQ = None
        asignaturasIEM = None
        asignaturasLAR = None
        asignaturasBasicas = None
        carrera = Carrera.objects.filter(nombre_carrera="Basicas").first()
        if(carrera):
            asignaturasBasicas = Asignatura.objects.filter(carrera = carrera)
        carrera = Carrera.objects.filter(nombre_carrera="ISI").first()
        if(carrera):
            asignaturasISI = Asignatura.objects.filter(carrera = carrera)
        carrera = Carrera.objects.filter(nombre_carrera="IQ").first()
        if(carrera):
            asignaturasIQ = Asignatura.objects.filter(carrera = carrera)
        carrera = Carrera.objects.filter(nombre_carrera="IEM").first()
        if(carrera):
            asignaturasIEM = Asignatura.objects.filter(carrera = carrera)
        carrera = Carrera.objects.filter(nombre_carrera="LAR").first()
        if(carrera):
            asignaturasLAR = Asignatura.objects.filter(carrera = carrera)
        context = {
                'asignaturasISI': asignaturasISI,
                'asignaturasIQ': asignaturasIQ,
                'asignaturasIEM': asignaturasIEM,
                'asignaturasLAR': asignaturasLAR,
                'asignaturasBasicas':asignaturasBasicas
                
            }  
        return render(request,'asignaturas/index.html', context)


    

@login_required
def AsignaturaDetailView(request, id, error = 'False'):
    print(error)
    mostrar_error = error == 'True'  
    asignatura = Asignatura.objects.get(id=id)  
    # Obtengo el nombre de la carrera
    carrera = Carrera.objects.get(id=asignatura.carrera_id)
    # Obtener planificaciones existentes
    usergroup = request.user.groups.values_list('name',flat = True)
    planificacionesDeAsignatura = Planificacion.objects.filter(asignatura=asignatura).filter(eliminada=False).exists()
    usuariosPlanificacion = PlanificacionUsuario.objects.filter(usuario_id = request.user.id)
    fechasParciales = None
    if "profesor" in  usergroup  :
        planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(eliminada=False).exclude(estado = 'R').order_by('fecha_creacion')
        asignaturasProfesor = Asignatura.objects.filter(profesor = request.user)
        for asig in asignaturasProfesor:
            planificacion = Planificacion.objects.filter(asignatura = asig).filter(datos_descriptivos__ciclo_lectivo = str(datetime.now().year) , estado = 'A').last()
            if(planificacion):
                if(planificacion.datos_descriptivos.ciclo_lectivo == str(datetime.now().year) and planificacion.estado == 'A'):
                    fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)
    elif "consejo" in  usergroup :
        planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(Q(estado = 'R') | Q(estado = 'A')).filter(eliminada=False).order_by('fecha_creacion')
        asignaturasProfesor = Asignatura.objects.filter(profesor = request.user)
        for asig in asignaturasProfesor:
            planificacion = Planificacion.objects.filter(asignatura = asig).filter(datos_descriptivos__ciclo_lectivo = str(datetime.now().year) , estado = 'A').last()
            if(planificacion):
                if(planificacion.datos_descriptivos.ciclo_lectivo == str(datetime.now().year) and planificacion.estado == 'A'):
                    fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)
    elif "jefe de carrera" in  usergroup :
        planificaciones = Planificacion.objects.filter(asignatura=asignatura)
        if (asignatura.profesor.filter(id = request.user.id).exists()):
            planificaciones = planificaciones.filter(eliminada=False).order_by('fecha_creacion')
        else:
            planificaciones = planificaciones.filter(Q(estado = 'R') | Q(estado = 'A')).filter(eliminada=False).order_by('fecha_creacion')

        asignaturasProfesor = Asignatura.objects.filter(profesor = request.user)
        for asig in asignaturasProfesor:
            planificacion = Planificacion.objects.filter(asignatura = asig).filter(datos_descriptivos__ciclo_lectivo = str(datetime.now().year) , estado = 'A').last()
            if(planificacion):
                if(planificacion.datos_descriptivos.ciclo_lectivo == str(datetime.now().year) and planificacion.estado == 'A'):
                    fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)
    elif "alumno" in usergroup:
        planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(estado = 'A').filter(eliminada=False).order_by('fecha_creacion')
        for up in usuariosPlanificacion:
            planificacion = Planificacion.objects.get(id = up.planificacion_id)
            if(planificacion):
                if(planificacion.datos_descriptivos.ciclo_lectivo == str(datetime.now().year) and planificacion.estado == 'A'):
                    fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)


    # Mandarle el form para crear planificaciones
    form = PlanificacionForm()  
    if(planificaciones):
        planificaciones = planificaciones.order_by('-fecha_creacion')

    calendarioAcademico = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')    
    
    calendario = viewCalendario.CreateCalendario(calendarioAcademico, fechasParciales)

    msgError = None
    if mostrar_error:
        msgError = "La planificacion tiene un problema y no es posible tomarla como referencia"
    context = {
            'planificaciones':planificaciones,
            'planificacionesDeAsignatura':planificacionesDeAsignatura,
            'asignatura': asignatura,
            'carrera':carrera,
            'form':form, 
            'usuariosPlanificacion':usuariosPlanificacion,
            'calendario': calendario,
            'error':msgError
        }
    return render(request,'asignaturas/detail.html',context)  

@login_required
def AsignaturaUpdate(request, id):  
    asignatura = Asignatura.objects.get(id=id)
    form = AsignaturaForm(instance = asignatura)
    if request.method == "POST":  
        form = AsignaturaForm(request.POST, instance = asignatura)  
        if form.is_valid():
            asig = form.save(commit=False)
            asig.save()
            form.save_m2m()
            return redirect('planificaciones:asignaturas')
    profesoresCarrera = User.objects.filter(carrera = asignatura.carrera)
    form.fields['profesor'].queryset = User.objects.filter(carrera = asignatura.carrera)
    form.fields['profesor'].choices  = [(user.id, f"{user.first_name} {user.last_name}") for user in form.fields['profesor'].queryset]
    context = {
        'asignatura': asignatura,
        'form':form,
        'profesoresCarrera':profesoresCarrera
    }      
    return render(request, 'asignaturas/update.html', context)  

@login_required
def AsignaturaDestroy(request, id):  
    asignatura = Asignatura.objects.get(id=id)  
    asignatura.delete()  
    return asignatura("/show") 

@login_required
def PapeleraView(request, id_asignatura):  
    asignatura = Asignatura.objects.get(id=id_asignatura)  
    carrera = Carrera.objects.get(id=asignatura.carrera_id)
    planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(eliminada=True).order_by('fecha_creacion')
    context = {
            'planificaciones':planificaciones,
            'asignatura': asignatura,
            'carrera':carrera, 
        }  
    return render(request,'asignaturas/papelera.html', context)   

@login_required 
def MandarAvisoFechaLimiteDePlanificacion(request):
    carreraUsuario = request.user.carrera.all()
    if(carreraUsuario.count()==1):
        carrera = Carrera.objects.get(id = carreraUsuario.first().id)
    form = AsignaturaCarreraForm()
    if request.method == 'POST':
        form = AsignaturaCarreraForm(request.POST)
        form.fields['asignaturas'].queryset = Asignatura.objects.filter(carrera=carrera)
        if form.is_valid():
            asignaturas = form.cleaned_data['asignaturas']
            comentario = form.cleaned_data['comentario']
            for asignatura in asignaturas:
                 ## Me conecto al servidor
                server = smtplib.SMTP('smtp-mail.outlook.com', 587)
                server.starttls()
                server.login("victoria060298@ca.frre.utn.edu.ar", "Vi02cto0$$")
                from_email = "victoria060298@ca.frre.utn.edu.ar"
                for usuario in asignatura.profesor.all():
                    to_email = usuario.email
                    message = comentario
                    message = MIMEText(message)
                    message["Content-Type"] = "text/plain; charset=UTF-8"
                    message['subject'] = 'Cambio de estado de la planificacion'
                    msg = message.as_string()
                    server.sendmail(from_email, to_email, msg)

                ##Cierro conexion al servidor
                server.quit()
            return redirect('planificaciones:asignaturas')
    else:
        form.fields['asignaturas'].queryset = Asignatura.objects.filter(carrera=carrera)
