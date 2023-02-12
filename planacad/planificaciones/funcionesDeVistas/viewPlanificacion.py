# Para usar los objetos y/o funciones de 'redirect'
import json
from django.shortcuts import render, redirect 
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime

## import model and form
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.modelos.modelFundamentacion import Fundamentacion
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.formularios.formPlanificacion import PlanificacionForm
from planificaciones.funcionesDeVistas import viewDatosDescriptivos
from planificaciones.funcionesDeVistas import viewFundamentacion
from planificaciones.validaciones import validacionSecciones
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import smtplib
from email.mime.text import MIMEText

##Define request for Planificacion   
@login_required
def PlanificacionNew(request, asignatura_id):  
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        planificaciones = Planificacion.objects.filter(asignatura_id = asignatura_id).filter(eliminada = False)
        current_year = datetime.now().year
        existePlanificacionAñoActual = False
        for planificacion in planificaciones:
            if(planificacion):
                if(planificacion.datos_descriptivos.ciclo_lectivo):
                    if(planificacion.datos_descriptivos.ciclo_lectivo == current_year):
                        existePlanificacionAñoActual = True 
                elif planificacion.fecha_creacion.year == current_year:
                    existePlanificacionAñoActual = True

        if not existePlanificacionAñoActual: 
            # create a form instance and populate it with data from the request:
            form = PlanificacionForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                print("form valid")
                # Creo una instancia y no lo guardo aun
                instance = form.save(commit=False)
                # Asigno la asignatura, no hace falta ir a buscar el objeto
                instance.asignatura_id = asignatura_id
                instance.estado = 'P'
                # Obtengo el id de carrera 
                asignatura = Asignatura.objects.get(id=asignatura_id) 
                print(asignatura)
                # Creo secciones vacías
                datosDescriptivos = DatosDescriptivos()  
                # Asigno la asignatura y carrera, no hace falta ir a buscar el objeto
                datosDescriptivos.asignatura_id = asignatura_id
                datosDescriptivos.carrera_id = asignatura.carrera_id
                # Guardo el objeto definitivamente
                datosDescriptivos.save()
                fundamentacion = Fundamentacion()
                # Guardo el objeto definitivamente
                fundamentacion.save()           
                # Vinculo los ids
                instance.datos_descriptivos_id = datosDescriptivos.id
                instance.fundamentacion_id = fundamentacion.id
                
                # Guardo el objeto definitivamente
                instance.save()
                return redirect('planificaciones:datosDescriptivos',id_planificacion = instance.id)
            # if a GET (or any other method) we'll create a blank form
            else:
                messages.error(request, 'Ha ocurrido un error pruebalo nuevamente')
                return redirect('planificaciones:asignaturaDetail',id = asignatura_id)
        else:
            messages.error(request, 'Ya existe una planificacion de este año')
            return redirect('planificaciones:asignaturaDetail',id = asignatura_id)

@login_required
def PlanificacionesView(request,idAsignatura):
    #Obtengo la asignatura
    asignatura = Asignatura.objects.get(id=idAsignatura)   
    #Busco las planificaciones de esa asignatura
    planificaciones = Planificacion.objects.filter(asignatura=asignatura)
    return render(request,"planificacion/index.html",{'planificaciones':planificaciones})  

@login_required
def PlanificacionDetailView(request, id): 
    planificacion = Planificacion.objects.get(id=id)
    return render(request,'planificacion/detail.html', {'planificacion':planificacion})  

@login_required
def PlanificacionUpdate(request, id):  
    planificacion = Planificacion.objects.get(id=id)  
    form = PlanificacionForm(request.POST, instance = planificacion)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'planificacion': planificacion})  

@login_required
def PlanificacionLogicDestroy(request, id):  
    mensaje_error = None
    try:
        print(id)
        planificacion = Planificacion.objects.get(id=id)
        planificacion.eliminada = True
        planificacion.save(update_fields=['eliminada'])
        return redirect('planificaciones:asignaturaDetail', id=planificacion.asignatura.id)

    except:
        mensaje_error="No se pudo eliminar la planificacion"
        return render(request, '/asignaturas/'+str(planificacion.asignatura.id), {'mensaje_error': mensaje_error})  


@login_required
def PlanificacionRestore(request, id):
    mensaje_error = None
    try:
        planificacionRestore = Planificacion.objects.get(id=id)
        planificaciones = Planificacion.objects.filter(asignatura_id = planificacionRestore.asignatura.id).filter(eliminada = False)
        if(planificacionRestore):
            if(planificacionRestore.datos_descriptivos.ciclo_lectivo):
                current_year = planificacionRestore.datos_descriptivos.ciclo_lectivo
            else:
                current_year = datetime.now().year
        
        existePlanificacionAñoActual = False
        for planificacion in planificaciones:
            if(planificacion.datos_descriptivos.ciclo_lectivo):
                if(planificacion.datos_descriptivos.ciclo_lectivo == current_year):
                        existePlanificacionAñoActual = True 
                elif planificacion.fecha_creacion.year == current_year:
                    existePlanificacionAñoActual = True

        if not existePlanificacionAñoActual:
            planificacionRestore.eliminada = False
            planificacionRestore.save(update_fields=['eliminada'])
            return redirect('planificaciones:asignaturaDetail', id=planificacionRestore.asignatura.id)
        else:
            messages.error(request, 'Ya existe una nueva planificacion de este año creada, puede eliminarla y luego restarurar esta')
            return redirect('planificaciones:papelera', id_asignatura=planificacionRestore.asignatura.id)
    except:
        mensaje_error = "No se pudo eliminar la planificacion"
        return redirect('planificaciones:asignaturaDetail', {'id': planificacionRestore.asignatura.id, 'mensaje_error': mensaje_error})

@login_required
def PlanificacionDestroy(request, id):  
    planificacion = Planificacion.objects.get(id=id)  
    planificacion.delete()  
    return redirect('planificaciones:papelera', id_asignatura=planificacion.asignatura.id)

@login_required
def AprobarPlanificacion(request, id):
    validacion_ok, validacion_bad, errores = validacionSecciones.ValidacionPlanificacion(id)
    if(validacion_ok):
        planificacion = Planificacion.objects.get(id=id)  
        form = PlanificacionForm(request.POST, instance = planificacion)  
        if form.is_valid():
            instance = form.save(commit=False)
            print(instance.estado)
            instance.estado = "A"
            print(instance.estado)  
            instance.save()


            ## Me conecto al servidor
            server = smtplib.SMTP('smtp-mail.outlook.com', 587)
            server.starttls()
            server.login("victoria060298@ca.frre.utn.edu.ar", "Vi02cto0$$")
            from_email = "victoria060298@ca.frre.utn.edu.ar"
            for usuario in planificacion.asignatura.profesor.all():
                to_email = usuario.email
                message = "Se ha aprobado la planificacion de " + planificacion.asignatura.nombre_materia + " de la comision " + str(planificacion.asignatura.comision) + " del año " + str(planificacion.datos_descriptivos.ciclo_lectivo) 
                message = MIMEText(message)
                message["Content-Type"] = "text/plain; charset=UTF-8"
                message['subject'] = 'Cambio de estado de la planificacion'
                msg = message.as_string()
                server.sendmail(from_email, to_email, msg)

            ##Cierro conexion al servidor
            server.quit()
            
        return redirect('planificaciones:datosDescriptivos', id_planificacion=planificacion.id)
    else:
        print("no todos los campos activos")
        data_json = json.dumps(errores)
        url = '/planificacion/' + str(id) + '/datos-descriptivos' + '?data=' + data_json
        return redirect(url)

@login_required
def RevisarPlanificacion(request, id):
    validacion_ok, validacion_bad, errores = validacionSecciones.ValidacionPlanificacion(id)
    if(validacion_ok):
        planificacion = Planificacion.objects.get(id=id)  
        form = PlanificacionForm(request.POST, instance = planificacion)  
        if form.is_valid():
            instance = form.save(commit=False)
            print(instance.estado)
            instance.estado = "R"
            print(instance.estado)  
            instance.save()

            ## Me conecto al servidor
            server = smtplib.SMTP('smtp-mail.outlook.com', 587)
            server.starttls()
            server.login("victoria060298@ca.frre.utn.edu.ar", "Vi02cto0$$")
            from_email = "victoria060298@ca.frre.utn.edu.ar"
            for usuario in planificacion.asignatura.profesor.all():
                to_email = usuario.email
                message = "Se ha mandado a revisar la planificacion de " + planificacion.asignatura.nombre_materia + " de la comision " + str(planificacion.asignatura.comision) + " del año " + str(planificacion.datos_descriptivos.ciclo_lectivo) 
                message = MIMEText(message)
                message["Content-Type"] = "text/plain; charset=UTF-8"
                message['subject'] = 'Cambio de estado de la planificacion'
                msg = message.as_string()
                server.sendmail(from_email, to_email, msg)

            ##Cierro conexion al servidor
            server.quit()


        return redirect('planificaciones:datosDescriptivos', id_planificacion=planificacion.id)
    else:
        print("no todos los campos activos")
        data_json = json.dumps(errores)
        url = '/planificacion/' + str(id) + '/datos-descriptivos' + '?data=' + data_json
        return redirect(url)

@login_required
def CorregirPlanificacion(request, id):
    planificacion = Planificacion.objects.get(id=id)  
    form = PlanificacionForm(request.POST, instance = planificacion)  
    if form.is_valid():
        instance = form.save(commit=False)
        print(instance.estado)
        instance.estado = "C"
        print(instance.estado)  
        instance.save()

        ## Me conecto al servidor
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login("victoria060298@ca.frre.utn.edu.ar", "Vi02cto0$$")
        from_email = "victoria060298@ca.frre.utn.edu.ar"
        for usuario in planificacion.asignatura.profesor.all():
            to_email = usuario.email
            message = "Se ha mandado a corregir la planificacion de " + planificacion.asignatura.nombre_materia + " de la comision " + str(planificacion.asignatura.comision) + " del año " + str(planificacion.datos_descriptivos.ciclo_lectivo) 
            message = MIMEText(message)
            message["Content-Type"] = "text/plain; charset=UTF-8"
            message['subject'] = 'Cambio de estado de la planificacion'
            msg = message.as_string()
            server.sendmail(from_email, to_email, msg)

        ##Cierro conexion al servidor
        server.quit()
        
    return redirect('planificaciones:datosDescriptivos', id_planificacion=planificacion.id)
    