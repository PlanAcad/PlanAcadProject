from django.db import models
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelSubCompetencia import SubCompetencia
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from planificaciones.modelos.modelBibliografia import Bibliografia
from planificaciones.modelos.modelEstrategiasEns import EstrategiasEns
from planificaciones.modelos.modelUnidad import Unidad



class PropuestaDesarrollo(models.Model): 
    actividad_dentro_aula = models.CharField(max_length=3000, null=True, blank=True)
    actividad_fuera_aula = models.CharField(max_length=3000, null=True, blank=True)
    tiempo_dentro_aula = models.CharField(max_length=50, null=True, blank=True)
    tiempo_fuera_aula = models.CharField(max_length=50, null=True, blank=True)
    modo_agrupamiento = models.CharField(max_length=500, null=True, blank=True)
    materiales_equipamiento = models.CharField(max_length=500, null=True, blank=True)



    # RELATIONS
    planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE)
    subcompetencias = models.ManyToManyField(SubCompetencia, blank=True, null=True)
    resultados_de_aprendizaje = models.ManyToManyField(ResultadoDeAprendizaje, blank=True ,null=True)
    unidades = models.ManyToManyField(Unidad, blank=True ,null=True)
    bibliografias = models.ManyToManyField(Bibliografia, blank=True, null=True )
    estrategias_ens = models.ManyToManyField(EstrategiasEns, blank=True, null=True )
    
    def __str__(self):
        return "%s" % (self.id)