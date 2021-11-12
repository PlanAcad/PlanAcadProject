from django.db import models


class EstrategiasEns(models.Model):
    key = models.CharField(max_length=3, null=False, blank=False)
    estrategia = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return "%s" % (self.estrategia)