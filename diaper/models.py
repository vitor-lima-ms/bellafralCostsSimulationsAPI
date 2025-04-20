from django.db import models

# Create your models here.

modelo_choices = [
    ('ABS BELLAFRAL CONFORT', 'ABS BELLAFRAL CONFORT'),
    ('ABS BELLAFRAL BASIC', 'ABS BELLAFRAL BASIC'),
    ('ABS BIG CONFORT', 'ABS BIG CONFORT'),
    ('FRALDA BELLAFRAL CONFORT', 'FRALDA BELLAFRAL CONFORT'),
    ('FRALDA BELLAFRAL BASIC', 'FRALDA BELLAFRAL BASIC'),
    ('FRALDA BIG CONFORT', 'FRALDA BIG CONFORT'),
]

tamanho_choices = [
    ('XG', 'XG'),
    ('G', 'G'),
    ('M', 'M'),
    ('TAMANHO ÚNICO', 'TAMANHO ÚNICO'),
]

class Diaper(models.Model):
    modelo = models.CharField(verbose_name='Modelo', max_length=100, choices=modelo_choices)
    identificador = models.CharField(verbose_name='Identificador', max_length=100)
    tamanho = models.CharField(verbose_name='Tamanho', max_length=100, choices=tamanho_choices)

    qtdCeluloseVirgem = models.DecimalField(verbose_name='Celulose virgem (Kg)', max_digits=10, decimal_places=4)
    qtdGel = models.DecimalField(verbose_name='Gel (Kg)', max_digits=10, decimal_places=4)
    qtdTnt162 = models.DecimalField(verbose_name='TNT 162 (m2)', max_digits=10, decimal_places=4, default=0)
    qtdTnt750 = models.DecimalField(verbose_name='TNT 750 (m2)', max_digits=10, decimal_places=4)
    qtdTnt780 = models.DecimalField(verbose_name='TNT 780 (m2)', max_digits=10, decimal_places=4)
    qtdFitaAdesiva = models.DecimalField(verbose_name='Fita adesiva (m)', max_digits=10, decimal_places=4)
    qtdElastico = models.DecimalField(verbose_name='Elastico (Kg)', max_digits=10, decimal_places=4)
    qtdBarreira = models.DecimalField(verbose_name='Barreira (m2)', max_digits=10, decimal_places=4)
    qtdPolietileno162 = models.DecimalField(verbose_name='Polietileno 162 (Kg)', max_digits=10, decimal_places=4,
                                            default=0)
    qtdPolietileno750 = models.DecimalField(verbose_name='Polietileno 750 (Kg)', max_digits=10, decimal_places=4,
                                            default=0)
    qtdPolietileno780 = models.DecimalField(verbose_name='Polietileno 780 (Kg)', max_digits=10, decimal_places=4)
    qtdHotMelt = models.DecimalField(verbose_name='Hot-Melt (Kg)', max_digits=10, decimal_places=4)
    qtdPorPacote = models.IntegerField(verbose_name='Quantidade de fraldas por pacote')

    percentPerdas = models.DecimalField(verbose_name='Perdas (%)', max_digits=10, decimal_places=4)

    precoEmbalagem = models.DecimalField(verbose_name='Embalagem (R$)', max_digits=10, decimal_places=4)
    precoFardoEncarte = models.DecimalField(verbose_name='Saco para fardos/Encarte (R$)', max_digits=10,
                                            decimal_places=4)

    percentComissao = models.DecimalField(verbose_name='Comissão (%)', max_digits=10, decimal_places=4)
    percentImpostos = models.DecimalField(verbose_name='Impostos (%)', max_digits=10, decimal_places=4)
    percentFrete = models.DecimalField(verbose_name='Frete (%)', max_digits=10, decimal_places=4)
    percentMargem = models.DecimalField(verbose_name='Margem de contribuição (%)', max_digits=10, decimal_places=4)
    percentST = models.DecimalField(verbose_name='ST (%)', max_digits=10, decimal_places=4)

    def __str__(self):
        return f'{self.modelo} {self.identificador} ({self.tamanho})'