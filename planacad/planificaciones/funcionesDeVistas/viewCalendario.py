from planificaciones.modelos.modelCalendario import Calendario
from datetime import datetime


def CreateCalendario(calendarioAcademico, parciales):
        calendarioConParciales = []
        if(calendarioAcademico):
            for calendario in calendarioAcademico:
                calen = Calendario(fecha = calendario.fecha.date() , hay_clase = calendario.hay_clase, actividades = [f'{calendario.get_actividad_display()}'])
                calendarioConParciales.append(calen)
            
        if(parciales):
            for parcial in parciales:
                existeLaFecha= False
                for calendario in calendarioConParciales:
                    if(parcial.fecha_clase == calendario.fecha):
                        calendario.actividades.append(f'{parcial.es_examen} + " de: " {parcial.planificacion.asignatura.nombre_materia}')
                        existeLaFecha = True
                
                if(not existeLaFecha):
                    calen = Calendario(fecha =parcial.fecha_clase , hay_clase = True, actividades = [f'{parcial.get_es_examen_display()} de {parcial.planificacion.asignatura.nombre_materia}'])
                    calendarioConParciales.append(calen)
        calendarioConParciales = sorted(calendarioConParciales, key=lambda x: x.fecha)   
        return calendarioConParciales
                    
            
            

