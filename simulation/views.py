from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from simulation.models import Simulation
from simulation.serializers import SimulationSerializer
from diaper.models import Diaper
from cost.models import Cost

# Create your views here.

class SimulationsAPIView(APIView):
    def get(self, request):
        simulations = Simulation.objects.all()
        serializer = SimulationSerializer(simulations, many=True)
        return Response(serializer.data)

    def post(self, request):
        diaper = Diaper.objects.get(id=request.data['fraldaObj'])
        cost = Cost.objects.get(id=request.data['custoObj'])

        """Calculando os Custos Unitários Totais por componente"""
        request.data['celuloseVirgemCUT'] = round(diaper.qtdCeluloseVirgem * cost.custoCeluloseVirgem, 4)
        request.data['gelCUT'] = round(diaper.qtdGel * cost.custoGel, 4)
        request.data['tnt162CUT'] = round(diaper.qtdTnt162 * cost.custoTnt162, 4)
        request.data['tnt750CUT'] = round(diaper.qtdTnt750 * cost.custoTnt750, 4)
        request.data['tnt780CUT'] = round(diaper.qtdTnt780 * cost.custoTnt780, 4)
        request.data['fitaAdesiva162CUT'] = round(diaper.qtdFitaAdesiva * cost.custoFitaAdesiva, 4)
        request.data['elasticoCUT'] = round(diaper.qtdElastico * cost.custoElastico, 4)
        request.data['barreiraCUT'] = round(diaper.qtdBarreira * cost.custoBarreira, 4)
        request.data['polietileno162CUT'] = round(diaper.qtdPolietileno162 * cost.custoPolietileno162, 4)
        request.data['polietileno750CUT'] = round(diaper.qtdPolietileno750 * cost.custoPolietileno750, 4)
        request.data['polietileno780CUT'] = round(diaper.qtdPolietileno780 * cost.custoPolietileno780, 4)
        request.data['hotMeltCUT'] = round(diaper.qtdHotMelt * cost.custoHotMelt, 4)

        """Calculando os Custos Totais sem Perdas"""
        request.data['fraldaCustoTotalSemPerdas'] = round(request.data['celuloseVirgemCUT'] + request.data['gelCUT'] +
                                                     request.data['tnt162CUT'] + request.data['tnt750CUT'] +
                                                     request.data['tnt780CUT'] + request.data['fitaAdesiva162CUT'] +
                                                     request.data['elasticoCUT'] + request.data['barreiraCUT'] +
                                                     request.data['polietileno162CUT'] + request.data['polietileno750CUT'] +
                                                     request.data['polietileno780CUT'] + request.data['hotMeltCUT'], 4)

        """Calculando os Custos Totais com Perdas"""
        request.data['fraldaCustoTotalComPerdas'] = round(request.data['fraldaCustoTotalSemPerdas']
                                                          * (1 + diaper.percentPerdas / 100))

        """Calculando o Custo do Pacote"""
        request.data['fraldaCustoPacote'] = round((request.data['fraldaCustoTotalComPerdas'] * diaper.qtdPorPacote) +
                                                  diaper.precoEmbalagem + diaper.precoFardoEncarte, 4)

        """Calculando o Custo Unitário Final"""
        request.data['fraldaCUF'] = round(request.data['fraldaCustoPacote'] / diaper.qtdPorPacote, 4)

        """Calculando o preço de venda"""
        request.data['precoVenda'] = round(request.data['fraldaCustoPacote'] /
                                           ((100 - diaper.percentComissao - diaper.percentImpostos -
                                             diaper.percentFrete - diaper.percentMargem) / 100), 4)

        """Calculando o preço de venda unitário"""
        request.data['precoVendaUnitario'] = round(request.data['precoVenda'] / diaper.qtdPorPacote, 4)

        """Calculando o preço de venda com ST"""
        request.data['precoVendaST'] = round(request.data['precoVenda'] * (1 + diaper.percentST) / 100, 4)

        """Calculando o preço de venda unitário com ST"""
        request.data['precoVendaUnitarioST'] = round(request.data['precoVendaST'] / diaper.qtdPorPacote, 4)

        serializer = SimulationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)