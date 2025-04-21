from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from cost.models import Cost
from diaper.models import Diaper
from simulation import functions


# Create your models here.

class Simulation(models.Model):
    custoObj = models.ForeignKey(verbose_name='Custo', on_delete=models.CASCADE, to=Cost)
    fraldaObj = models.ForeignKey(verbose_name='Fralda', on_delete=models.CASCADE, to=Diaper)

    celuloseVirgemCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    gelCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    tnt162CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    tnt750CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    tnt780CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    fitaAdesivaCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    elasticoCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    barreiraCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    polietileno162CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    polietileno750CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    polietileno780CUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    hotMeltCUT = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)

    fraldaCustoTotalSemPerdas = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    fraldaCustoTotalComPerdas = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    fraldaCustoPacote = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    fraldaCUF = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)

    precoVenda = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    precoVendaUnitario = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    precoVendaST = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)
    precoVendaUnitarioST = models.DecimalField(max_digits=10, decimal_places=4, default=0, blank=True)

    def __str__(self):
        return f'{self.fraldaObj.modelo} ({self.fraldaObj.tamanho}) - {self.custoObj.identificador}'

@receiver(post_save, sender=Diaper)
def calculations(sender, **kwargs):
    simulacoes = Simulation.objects.all()

    for simulacao in simulacoes:
        functions.calcular_custo_unitario_total_por_componente(simulacao)
        functions.calcular_custo_total_sem_perdas(simulacao)
        functions.calcular_custo_total_com_perdas(simulacao)
        functions.calcular_custo_pacote(simulacao)
        functions.calcular_custo_unitario_final(simulacao)
        functions.calcular_preco_venda(simulacao)
        functions.calcular_preco_venda_unitario(simulacao)
        functions.calcular_preco_venda_st(simulacao)
        functions.calcular_preco_venda_unitario_st(simulacao)

@receiver(post_save, sender=Cost)
def calculations(sender, **kwargs):
    simulacoes = Simulation.objects.all()

    for simulacao in simulacoes:
        functions.calcular_custo_unitario_total_por_componente(simulacao)
        functions.calcular_custo_total_sem_perdas(simulacao)
        functions.calcular_custo_total_com_perdas(simulacao)
        functions.calcular_custo_pacote(simulacao)
        functions.calcular_custo_unitario_final(simulacao)
        functions.calcular_preco_venda(simulacao)
        functions.calcular_preco_venda_unitario(simulacao)
        functions.calcular_preco_venda_st(simulacao)
        functions.calcular_preco_venda_unitario_st(simulacao)