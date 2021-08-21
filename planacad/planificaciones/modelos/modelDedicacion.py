from django.db import models

class Dedicacion(models.Model): 
   id = models.AutoField(primary_key=True) 
   dedicacionPosible=[
    ('1','test'),
    ('2','test2')
    ]
   cursado = models.CharField( null=True, blank=True,choices=dedicacionPosible, default="1")

   def __str__(self) -> str:
       return self.cursado