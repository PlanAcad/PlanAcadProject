from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos  
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra 
from planificaciones.modelos.modelFundamentacion import Fundamentacion 
from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior 
from planificaciones.modelos.modelCompetencia import Competencia
from planificaciones.modelos.modelSubCompetencia import SubCompetencia 
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje 
from planificaciones.modelos.modelPropuestaDesarrollo import PropuestaDesarrollo 
from planificaciones.modelos.modelActividad import Actividad 
from planificaciones.modelos.modelClase import Clase 
from planificaciones.modelos.modelBibliografia import Bibliografia 
from planificaciones.modelos.modelWebgrafia import Webgrafia 
from planificaciones.modelos.modelContenido import Contenido 
from planificaciones.validaciones import validacionSecciones
import json
import io
from django.http import FileResponse
from django.shortcuts import render, redirect 
from reportlab.pdfgen import canvas

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import Table, TableStyle, Paragraph, PageBreak, SimpleDocTemplate, Spacer, ListFlowable, ListItem, KeepTogether
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize

PAGE_HEIGHT=defaultPageSize[1]; 
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()

styleSectionTitle = ParagraphStyle(
        'titleSection',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=12,
        spaceAfter=6,
    )

styleSectionSubtitle = ParagraphStyle(
        'titleSection',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        spaceAfter=6,
    )

styleTitleTable = ParagraphStyle(
        'titleSection',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        spaceAfter=6,
    )

styleBlackText = ParagraphStyle(
    'blackText',
    fontName='Helvetica-Bold',
)


def print_datos_descriptivos(Story,datos_descriptivos):
    p = Paragraph("1. Datos descriptivos:", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    data = [
        ['Institución', datos_descriptivos.institucion],
        ['Carrera', datos_descriptivos.carrera.nombre_carrera],
        ['Departamento', datos_descriptivos.departamento],
        ['Area/Bloque', datos_descriptivos.area_bloque],
        ['Asignatura', datos_descriptivos.asignatura.nombre_materia],
        ['Nivel', datos_descriptivos.nivel],
        ['Ciclo Lectivo', str(datos_descriptivos.ciclo_lectivo)],
        ['Carga Horaria Total', str(datos_descriptivos.carga_horaria_total)],
        ['Carga Horaria Semanal', str(datos_descriptivos.carga_horaria_semanal)],
        ['Cursado', datos_descriptivos.cursado],
        ]

    t = Table(data, colWidths=200)
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP')
                        ]))

    Story.append(t)
    Story.append(Spacer(1,0.2*inch))

def print_estructura_catedra(Story, estructuras_catedra):
    p = Paragraph("2. Estructura de la cátedra:", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    data = [
        [Paragraph("Nombre", styleSectionSubtitle), Paragraph('Categoría', styleSectionSubtitle), Paragraph('Dedicación', styleSectionSubtitle), Paragraph('Situación', styleSectionSubtitle), Paragraph('Tareas/Funciones', styleSectionSubtitle)],
    ]

    style = styles["Normal"]
    for estructura in estructuras_catedra:

        p_tareas = []
        for tarea in estructura.tareas.all():
            t = Paragraph(tarea.tarea_funcion, style, bulletText='-')
            p_tareas.append(t)

        new_row = [estructura.profesor.nombre + ' ' + estructura.profesor.apellido, estructura.categoria.categoria, estructura.dedicacion.dedicacion, estructura.situacion.situacion, p_tareas]
        data.append(new_row)

    t = Table(data)
    t.setStyle(
        TableStyle(
            [   ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP')
            ]
            )
        )
    
    Story.append(t)
    Story.append(Spacer(1,0.2*inch))

def print_fundamentacion(Story, fundamentacion):
    p = Paragraph("3. Fundamentación:", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    style = styles["Normal"]
    p = Paragraph(fundamentacion, style)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

def print_resultados_aprendizaje_previos(Story, resultados_aprendizaje_previos):
    titleSection = "4. Resultados de Aprendizajes previos requeridos para iniciar/ continuar el desarrollo de los Resultados de Aprendizaje de la asignatura en relación con el nivel de aporte a las sub-competencias y Competencias."
    p = Paragraph(titleSection, styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    data = [
        [Paragraph('Asignaturas Aprobadas y/o Regularizadas', styleTitleTable), Paragraph('Resultados de Aprendizaje Alcanzados', styleTitleTable)],
    ]

    style = styles["Normal"]
    for resultado in resultados_aprendizaje_previos:
        new_row = [Paragraph(resultado.asignatura.nombre_materia, style), Paragraph(resultado.resultado.resultado, style)]
        data.append(new_row)

    t = Table(data)
    t.setStyle(
        TableStyle(
            [   ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP')

            ]
            )
        )
    
    Story.append(t)
    Story.append(Spacer(1,0.2*inch))

def print_competencias(Story, competencias):
    p = Paragraph("5. competencias y capacidades vinculadas con la Asignatura.", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))


    data = [
        [Paragraph('Tipo de competencia', styleTitleTable), Paragraph('Competencias', styleTitleTable), Paragraph('Sub-competencias', styleTitleTable)],
    ]

    style = styles["Normal"]
    
    for competencia in competencias:

        p_subcompetencias = []
        for subcompetencia in competencia.subcompetencia_set.all():
            p_subcompetencia = Paragraph(subcompetencia.descripcion or "", style, bulletText='-')
            p_subcompetencias.append(p_subcompetencia)
        new_row = [Paragraph(competencia.get_tipo_competencia_display(), style), Paragraph(competencia.descripcion or "", style), p_subcompetencias]
        data.append(new_row)

    t = Table(data)
    t.setStyle(
        TableStyle(
            [   ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP')

            ]
            )
        )
    
    Story.append(t)
    Story.append(Spacer(1,0.2*inch))

def print_propuesta_desarrollo(Story, resultados_aprendizaje, propuestas_desarrollo):
    p = Paragraph("6. Propuesta para el desarrollo de los procesos de enseñanza y Aprendizaje.", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    # ------------ 
    # RESULTADOS DE APRENDIZAJE
    # ------------ 
    p = Paragraph("Resultados de aprendizajes.", styleSectionSubtitle)
    Story.append(p)

    data = [
        [Paragraph('Resultado de aprendizaje', styleTitleTable), Paragraph('Resultados de aprendizaje alcanzados', styleTitleTable)],
    ]

    style = styles["Normal"]
    for index, resultado in enumerate(resultados_aprendizaje):
        new_row = [Paragraph('R' + str(index+1), style), Paragraph(resultado.resultado, style)]
        data.append(new_row)

    t = Table(data)
    t.setStyle(
        TableStyle(
            [   ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP')

            ]
            )
        )
    
    Story.append(t)
    Story.append(Spacer(1,0.2*inch))

    # ------------ 
    # PROPUESTAS DE DESARROLLO
    # ------------ 
    p = Paragraph("Propuestas de desarrollo.", styleSectionSubtitle)
    Story.append(p)

    data = [
        [Paragraph('Sub Comp.', styleTitleTable), Paragraph('RA', styleTitleTable), Paragraph('Unidades Tematicas', styleTitleTable), Paragraph('AFDAV', styleTitleTable), Paragraph('AFFDAV', styleTitleTable), Paragraph('THRDAV', styleTitleTable), Paragraph('THRFAV', styleTitleTable), Paragraph('Bibliografia propuesta por RA', styleTitleTable), Paragraph('Estrategias de enseñanza', styleTitleTable), Paragraph('Modo de agrupamiento', styleTitleTable), Paragraph('Materiales y/o equipamiento', styleTitleTable)]
    ]


    style = styles["Normal"]
    for propuesta in propuestas_desarrollo:

        p_subcompetencias = []
        for subcompetencia in propuesta.subcompetencias.all():
            p_subcompetencia = Paragraph(subcompetencia.descripcion, style, bulletText='-')
            p_subcompetencias.append(p_subcompetencia)

        p_resultados_aprendizaje = []
        for resultado in propuesta.resultados_de_aprendizaje.all():
            p_resultado = Paragraph(resultado.resultado, style, bulletText='-')
            p_resultados_aprendizaje.append(p_resultado)

        p_unidades = []
        for unidad in propuesta.unidades.all():
            p_unidad = Paragraph(unidad.descripcion, style, bulletText='-')
            p_unidades.append(p_unidad)

        p_bibliografias = []
        for bibliografia in propuesta.bibliografias.all():
            p_bibliografia = Paragraph(bibliografia.autor + ', ' + bibliografia.titulo_libro, style, bulletText='-')
            p_bibliografias.append(p_bibliografia)

        p_estrategias_ens = []
        for estrategia in propuesta.estrategias_ens.all():
            p_estrategia = Paragraph(estrategia.estrategia, style, bulletText='-')
            p_estrategias_ens.append(p_estrategia)
        


        new_row = [p_subcompetencias, p_resultados_aprendizaje, p_unidades, Paragraph(propuesta.actividad_dentro_aula, style), Paragraph(propuesta.actividad_fuera_aula, style), Paragraph(propuesta.tiempo_dentro_aula, style), Paragraph(propuesta.tiempo_fuera_aula, style), p_bibliografias, p_estrategias_ens, Paragraph(propuesta.modo_agrupamiento or "", style), Paragraph(propuesta.materiales_equipamiento or "", style)]
        data.append(new_row)

    t = Table(data, colWidths=40)
    t.setStyle(
        TableStyle(
            [   ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP')
            ]
            )
        )
    
    Story.append(t)
    Story.append(Spacer(1,0.2*inch))

def print_sistema_evaluacion(Story, actividades):
    p = Paragraph("7. Sistema de evaluación", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))


    data = [
        [Paragraph('Tipo', styleTitleTable), Paragraph('Actividades de evaluación', styleTitleTable), Paragraph('Unidad tematica', styleTitleTable), Paragraph('Lugar/plataformas', styleTitleTable), Paragraph('Indicadores de logro', styleTitleTable), Paragraph('RA', styleTitleTable), Paragraph('Tec. de Evaluación', styleTitleTable)],
    ]

    style = styles["Normal"]
    for actividad in actividades:

        p_resultados_aprendizaje = []
        for resultado in actividad.resultados_de_aprendizaje.all():
            p_resultado_aprendizaje = Paragraph(resultado.resultado, style, bulletText='-')
            p_resultados_aprendizaje.append(p_resultado_aprendizaje)

        new_row = [Paragraph(str(actividad.tipo_de_evaluacion.get_tipo_display()), style), Paragraph(actividad.get_actividad_display(), style), Paragraph(actividad.unidad_tematica, style), Paragraph(actividad.lugar, style), Paragraph(actividad.indicadores_de_logro, style), p_resultados_aprendizaje, Paragraph(actividad.tecnicas_de_evaluacion, style)]
        data.append(new_row)

    t = Table(data)
    t.setStyle(
        TableStyle(
            [   ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP')

            ]
            )
        )
    
    Story.append(t)
    Story.append(Spacer(1,0.2*inch))

def print_condicion_aprobacion(Story, condicion_aprobacion_directa, condicion_aprobacion_cursada):
    p = Paragraph("7.1 Condición aprobación directa", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    style = styles["Normal"]
    p = Paragraph(condicion_aprobacion_directa or "", style)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    p = Paragraph("7.2 Condición aprobación cursada", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    p = Paragraph(condicion_aprobacion_cursada or "", style)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

def print_cronograma(Story, clases):
    p = Paragraph("8. Cronograma", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))


    data = [
        [Paragraph('Profesor a cargo de la clase', styleTitleTable), Paragraph('Lugar de desarrollo de clase', styleTitleTable), Paragraph('Fecha y número de semana/clase', styleTitleTable), Paragraph('Unidad temática', styleTitleTable), Paragraph('Cantidad de tareas por clase/semana', styleTitleTable), Paragraph('RA', styleTitleTable)],
    ]

    style = styles["Normal"]
    for clase in clases:

        p_profesores = []
        for profesor in clase.profesor_a_cargo.all():
            p_profesor = Paragraph(profesor.nombre + ', ' + profesor.apellido, style, bulletText='-')
            p_profesores.append(p_profesor)

        p_unidades = []
        for contenido in clase.unidad_tematica_o_tema.all():
            p_unidad = Paragraph(contenido.unidad.titulo, style, bulletText='-')
            p_unidades.append(p_unidad)
        
        if clase.es_examen != 'NA':
            p_unidades.append(
                Paragraph(clase.get_es_examen_display() or "", styleBlackText))

        p_resultados = []
        for resultado in clase.resultado_de_aprendizaje.all():
            p_resultado = Paragraph(resultado.resultado, style, bulletText='-')
            p_resultados.append(p_resultado)

        new_row = [
            p_profesores, Paragraph(clase.lugar_desarrollo_de_clase or "", style), 
            [
                Paragraph(clase.fecha_clase.strftime("%m/%d/%Y") or "", style), 
                Paragraph(clase.numero_de_clase_o_semana or "", style)
            ], 
            p_unidades, Paragraph(str(clase.cantidad_tareas) or "", style), 
            p_resultados
        ]
        data.append(new_row)

    t = Table(data)
    t.setStyle(
        TableStyle(
            [   ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP')

            ]
            )
        )
    
    Story.append(t)
    Story.append(Spacer(1,0.2*inch))

def print_bibliografia(Story, bibliografias):
    p = Paragraph("9. Bibliografia", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    style = styles["Normal"]
    for bibliografia in bibliografias:
        autor = bibliografia.autor or ""
        titulo_libro = bibliografia.titulo_libro or ""
        editor = bibliografia.editor or ""
        año_publicacion = bibliografia.año_publicacion or ""
        nombre_capitulo = bibliografia.nombre_capitulo or ""
        ubicacion = bibliografia.ubicacion or ""
        bibliografia_description = autor + ', ' + titulo_libro + ', ' + editor + ', ' + año_publicacion + ', ' + nombre_capitulo + ', ' + ubicacion + '.'

        p = Paragraph(bibliografia_description, style, bulletText='.')
        Story.append(p)

    Story.append(Spacer(1,0.2*inch))

def print_webgrafia(Story, webgrafias):
    p = Paragraph("10. Webgrafia", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    style = styles["Normal"]
    for webgrafia in webgrafias:
        autor = webgrafia.autor or ""
        titulo_publicacion = webgrafia.titulo_publicacion or ""
        nombre_pagina = webgrafia.nombre_pagina or ""
        fecha_publicacion = webgrafia.fecha_publicacion.strftime("%m/%d/%Y") or ""
        link_pagina = webgrafia.link_pagina or ""
        webgrafia_description = autor + ', ' + titulo_publicacion + ', ' + nombre_pagina + ', ' + fecha_publicacion + ', ' + link_pagina + '.'

        p = Paragraph(webgrafia_description, style, bulletText='.')
        Story.append(p)

    Story.append(Spacer(1,0.2*inch))

def print_contenido(Story, contenidos):
    p = Paragraph("11. Contenido", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    style = styles["Normal"]
    for contenido in contenidos:
        p = Paragraph("Unidad "+ str(contenido.unidad.numero) + ": " + contenido.unidad.titulo, styleSectionSubtitle)
        Story.append(p)

        p = Paragraph("<b>Objetivos:</b>", style)
        Story.append(p)
        p = Paragraph(contenido.objetivos, style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))

        p = Paragraph("<b>Contenido:</b>", style)
        Story.append(p)
        p = Paragraph(contenido.contenido, style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))

        p = Paragraph("<b>Carga horaria: </b>" + contenido.carga_horaria, style)
        # p = Paragraph("Carga horaria:", style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))

def print_distribucion_tareas(Story, numero_comisiones, numero_estudiantes, profesores, profesores_auxiliares):
    p = Paragraph("12. Distribucion de tareas", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    style = styles["Normal"]
    p = Paragraph("Número de comisiones: " + str(numero_comisiones), style)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    p = Paragraph("Número de estudiantes por comisión: " + str(numero_estudiantes), style)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    # ------------ 
    # PROFESORES TITULARES
    # ------------ 
    p = Paragraph("Nómina de profesores", styleSectionSubtitle)
    Story.append(p)
    data = [
        [Paragraph('Nombre y apellido del docente', styleTitleTable), Paragraph('Categoría', styleTitleTable), Paragraph('Situación de revista y/o condición', styleTitleTable), Paragraph('Designación', styleTitleTable), Paragraph('Actividad que cumple y comisión', styleTitleTable)],
    ]

    for detalle_profesor in profesores:
        new_row = [Paragraph(detalle_profesor.profesor.nombre + ', ' + detalle_profesor.profesor.apellido, style), Paragraph(str(detalle_profesor.categoria), style), Paragraph(str(detalle_profesor.situacion), style), Paragraph(str(detalle_profesor.dedicacion), style), Paragraph(detalle_profesor.actividades or "", style)]
        data.append(new_row)
        
    t = Table(data)
    t.setStyle(
        TableStyle(
            [   ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP')

            ]
            )
        )
    
    Story.append(t)
    Story.append(Spacer(1,0.2*inch))


    # ------------ 
    # PROFESORES AUXILIARES
    # ------------ 
    p = Paragraph("Nómina de auxiliares", styleSectionSubtitle)
    Story.append(p)
    data = [
        [Paragraph('Nombre y apellido del docente', styleTitleTable), Paragraph('Categoría', styleTitleTable), Paragraph('Situación de revista y/o condición', styleTitleTable), Paragraph('Designación', styleTitleTable), Paragraph('Actividad que cumple y comisión', styleTitleTable)],
    ]

    for detalle_profesor in profesores_auxiliares:
        new_row = [Paragraph(detalle_profesor.profesor.nombre + ', ' + detalle_profesor.profesor.apellido, style), Paragraph(str(detalle_profesor.categoria), style), Paragraph(str(detalle_profesor.situacion), style), Paragraph(str(detalle_profesor.dedicacion), style), Paragraph(detalle_profesor.actividades or "", style)]
        data.append(new_row)
        
    t = Table(data)
    t.setStyle(
        TableStyle(
            [   ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP')

            ]
            )
        )
    
    Story.append(t)
    Story.append(Spacer(1,0.2*inch))

def print_justificacion_ordenanza(Story, justificacion_ordenanza):
    p = Paragraph("13. Justificación de ordenanza 604", styleSectionTitle)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    style = styles["Normal"]
    p = Paragraph(justificacion_ordenanza or "", style)
    Story.append(p)
    Story.append(Spacer(1,0.2*inch))

    
        

    


def Exportar(request, id_planificacion):  
    data =None 
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data_json = request.GET.get('data')
    if(data_json):
        data = json.loads(data_json)
    context = {
        'planificacion': planificacion,
        'errores': data
    }

    return render(request, "exportar/index.html", context) 




# Title = "Hello world"
pageinfo = "Planificación"

# STLYES AND CONTENT FOR FIRST PAGE
def myFirstPage(canvas, doc):
    canvas.setTitle('Planificación')
    canvas.saveState()
    # canvas.setFont('Times-Bold',16)
    # canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    # canvas.setFont('Times-Roman',9)
    # canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
    canvas.restoreState()

# STLYES AND CONTENT FOR LATER PAGES
def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()


# VIEW TO OPEN AND DOWNLOAD PDF
def DownloadPDF(request, id_planificacion):
    validacion_ok, validacion_bad, errores = validacionSecciones.ValidacionPlanificacion(id_planificacion)
    if(validacion_ok):
        planificacion = Planificacion.objects.get(id=id_planificacion)
        datos_descriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos.id)
        estructuras_catedra = DetalleProfesorCatedra.objects.filter(planificacion = planificacion)
        fundamentacion = Fundamentacion.objects.get(id=planificacion.fundamentacion_id)
        resultados_aprendizaje_previos = ResultadoDeAprendizajeAnterior.objects.filter(planificacion=planificacion)
        competencias = Competencia.objects.filter(planificacion = planificacion)

        resultados_aprendizaje = ResultadoDeAprendizaje.objects.filter(planificacion=planificacion) 
        resultados_aprendizaje_materia = resultados_aprendizaje.filter(asignatura=planificacion.asignatura).order_by('id')
        propuestas_desarrollo = PropuestaDesarrollo.objects.filter(planificacion=planificacion) 

        actividades = Actividad.objects.filter(planificacion=planificacion) 

        clases = Clase.objects.filter(planificacion=planificacion)

        bibliografias = Bibliografia.objects.filter(planificacion=planificacion) 
        webgrafias = Webgrafia.objects.filter(planificacion=planificacion)  

        contenidos = Contenido.objects.filter(planificacion=planificacion).order_by('id')  

        detalles_profesores_catedra = DetalleProfesorCatedra.objects.filter(planificacion = planificacion) 
        profesores =  detalles_profesores_catedra.filter(categoria__categoria = "Titular") | detalles_profesores_catedra.filter(categoria__categoria = "Adjunto")
        profesores_auxiliares =  detalles_profesores_catedra.exclude(categoria__categoria = "Titular").exclude(categoria__categoria = "Adjunto")



        # ------------ 
        # GENERATE PDF
        # ------------ 
        doc = SimpleDocTemplate("planificacion.pdf")
        # Story = [Spacer(1,2*inch)]
        Story = []

        print_datos_descriptivos(Story=Story, datos_descriptivos=datos_descriptivos)
        print_estructura_catedra(Story=Story, estructuras_catedra=estructuras_catedra)
        print_fundamentacion(Story=Story, fundamentacion=fundamentacion.fundamentos)
        print_resultados_aprendizaje_previos(Story=Story, resultados_aprendizaje_previos=resultados_aprendizaje_previos)
        print_competencias(Story=Story, competencias=competencias)
        print_propuesta_desarrollo(Story=Story, resultados_aprendizaje=resultados_aprendizaje_materia, propuestas_desarrollo=propuestas_desarrollo)
        print_sistema_evaluacion(Story=Story, actividades=actividades)
        print_condicion_aprobacion(Story=Story, condicion_aprobacion_directa= planificacion.condicion_aprobacion_directa,condicion_aprobacion_cursada=planificacion.condicion_aprobacion_cursada)
        print_cronograma(Story=Story, clases = clases)
        print_bibliografia(Story=Story, bibliografias = bibliografias)
        print_webgrafia(Story=Story, webgrafias = webgrafias)
        print_contenido(Story=Story, contenidos = contenidos)
        print_distribucion_tareas(Story=Story, numero_comisiones = planificacion.numero_comisiones, numero_estudiantes = planificacion.numero_estudiantes_comision, profesores = profesores, profesores_auxiliares = profesores_auxiliares)
        print_justificacion_ordenanza(Story=Story, justificacion_ordenanza = planificacion.justificacion_ordenanza)


        # ------------ 
        # CREATE PDF
        # ------------ 
        doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)


        # ------------ 
        # TO OPEN PDF IN BROWSER
        # ------------ 
        return FileResponse(open('planificacion.pdf', 'rb'), as_attachment=True, content_type='application/pdf', filename='planificacion.pdf')
    else:
        print("no todos los campos activos")
        data_json = json.dumps(errores)
        url = '/planificacion/' + str(id_planificacion) + '/exportar' + '?data=' + data_json
        return redirect(url)





# VIEW TO OPEN AND DOWNLOAD PDF
def PrintPDF(request, id_planificacion):
    validacion_ok, validacion_bad, errores = validacionSecciones.ValidacionPlanificacion(id_planificacion)
    if(validacion_ok):
        planificacion = Planificacion.objects.get(id=id_planificacion)
        datos_descriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos.id)
        estructuras_catedra = DetalleProfesorCatedra.objects.filter(planificacion = planificacion)
        fundamentacion = Fundamentacion.objects.get(id=planificacion.fundamentacion_id)
        resultados_aprendizaje_previos = ResultadoDeAprendizajeAnterior.objects.filter(planificacion=planificacion)
        competencias = Competencia.objects.filter(planificacion = planificacion)

        resultados_aprendizaje = ResultadoDeAprendizaje.objects.filter(planificacion=planificacion) 
        resultados_aprendizaje_materia = resultados_aprendizaje.filter(asignatura=planificacion.asignatura).order_by('id')
        propuestas_desarrollo = PropuestaDesarrollo.objects.filter(planificacion=planificacion) 

        actividades = Actividad.objects.filter(planificacion=planificacion) 

        clases = Clase.objects.filter(planificacion=planificacion)

        bibliografias = Bibliografia.objects.filter(planificacion=planificacion) 
        webgrafias = Webgrafia.objects.filter(planificacion=planificacion)  

        contenidos = Contenido.objects.filter(planificacion=planificacion).order_by('id')  

        detalles_profesores_catedra = DetalleProfesorCatedra.objects.filter(planificacion = planificacion) 
        profesores =  detalles_profesores_catedra.filter(categoria__categoria = "Titular") | detalles_profesores_catedra.filter(categoria__categoria = "Adjunto")
        profesores_auxiliares =  detalles_profesores_catedra.exclude(categoria__categoria = "Titular").exclude(categoria__categoria = "Adjunto")



        # ------------ 
        # GENERATE PDF
        # ------------ 
        doc = SimpleDocTemplate("planificacion.pdf")
        # Story = [Spacer(1,2*inch)]
        Story = []

        print_datos_descriptivos(Story=Story, datos_descriptivos=datos_descriptivos)
        print_estructura_catedra(Story=Story, estructuras_catedra=estructuras_catedra)
        print_fundamentacion(Story=Story, fundamentacion=fundamentacion.fundamentos)
        print_resultados_aprendizaje_previos(Story=Story, resultados_aprendizaje_previos=resultados_aprendizaje_previos)
        print_competencias(Story=Story, competencias=competencias)
        print_propuesta_desarrollo(Story=Story, resultados_aprendizaje=resultados_aprendizaje_materia, propuestas_desarrollo=propuestas_desarrollo)
        print_sistema_evaluacion(Story=Story, actividades=actividades)
        print_condicion_aprobacion(Story=Story, condicion_aprobacion_directa= planificacion.condicion_aprobacion_directa,condicion_aprobacion_cursada=planificacion.condicion_aprobacion_cursada)
        print_cronograma(Story=Story, clases = clases)
        print_bibliografia(Story=Story, bibliografias = bibliografias)
        print_webgrafia(Story=Story, webgrafias = webgrafias)
        print_contenido(Story=Story, contenidos = contenidos)
        print_distribucion_tareas(Story=Story, numero_comisiones = planificacion.numero_comisiones, numero_estudiantes = planificacion.numero_estudiantes_comision, profesores = profesores, profesores_auxiliares = profesores_auxiliares)
        print_justificacion_ordenanza(Story=Story, justificacion_ordenanza = planificacion.justificacion_ordenanza)


        # ------------ 
        # CREATE PDF
        # ------------ 
        doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)


        # ------------ 
        # TO OPEN PDF IN BROWSER
        # ------------ 
        return FileResponse(open('planificacion.pdf', 'rb'), as_attachment=False, content_type='application/pdf', filename='planificacion.pdf')
    else: 
        print("no todos los campos activos")
        data_json = json.dumps(errores)
        url = '/planificacion/' + str(id_planificacion) + '/exportar' + '?data=' + data_json
        return redirect(url)












