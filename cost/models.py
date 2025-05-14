from django.db import models

# Create your models here.

class Cost(models.Model):
    identificador = models.CharField(max_length=100, blank=True, null=True)

    custoCeluloseVirgem = models.DecimalField(verbose_name='Celulose virgem (R$)', max_digits=10, decimal_places=4, blank=True, null=True)
    custoGel = models.DecimalField(verbose_name='Gel (R$)', max_digits=10, decimal_places=4, blank=True, null=True)
    custoTnt162 = models.DecimalField(verbose_name='TNT 162 (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)
    custoTnt750 = models.DecimalField(verbose_name='TNT 750 (R$)', max_digits=10, decimal_places=4, blank=True, null=True)
    custoTnt780 = models.DecimalField(verbose_name='TNT 780 (R$)', max_digits=10, decimal_places=4, blank=True, null=True)
    custoFitaAdesiva = models.DecimalField(verbose_name='Fita adesiva (R$)', max_digits=10, decimal_places=4, blank=True, null=True)
    custoElastico = models.DecimalField(verbose_name='Elastico (R$)', max_digits=10, decimal_places=4, blank=True, null=True)
    custoBarreira = models.DecimalField(verbose_name='Barreira (R$)', max_digits=10, decimal_places=4, blank=True, null=True)
    custoPolietileno162 = models.DecimalField(verbose_name='Polietileno 162 (R$)', max_digits=10, decimal_places=4,
                                              default=0, blank=True, null=True)
    custoPolietileno750 = models.DecimalField(verbose_name='Polietileno 750 (R$)', max_digits=10, decimal_places=4,
                                              default=0, blank=True, null=True)
    custoPolietileno780 = models.DecimalField(verbose_name='Polietileno 780 (R$)', max_digits=10, decimal_places=4, blank=True, null=True)
    custoHotMelt = models.DecimalField(verbose_name='Hot-Melt (R$)', max_digits=10, decimal_places=4, blank=True, null=True)

    def __str__(self):
        return f'{self.identificador}'