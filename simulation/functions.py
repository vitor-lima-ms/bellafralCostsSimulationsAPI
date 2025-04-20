from simulation.models import Simulation

def calcular_custo_unitario_total_por_componente(simulation):
    simulation.celuloseVirgemCUT = round(simulation.custoObj.custoCeluloseVirgem * simulation.fraldaObj.qtdCeluloseVirgem, 4)
    simulation.gelCUT = round(simulation.custoObj.custoGel * simulation.fraldaObj.qtdGel, 4)
    simulation.tnt162CUT = round(simulation.custoObj.custoTnt162 * simulation.fraldaObj.qtdTnt162, 4)
    simulation.tnt750CUT = round(simulation.custoObj.custoTnt750 * simulation.fraldaObj.qtdTnt750, 4)
    simulation.tnt780CUT = round(simulation.custoObj.custoTnt780 * simulation.fraldaObj.qtdTnt780, 4)
    simulation.fitaAdesivaCUT = round(simulation.custoObj.custoFitaAdesiva * simulation.fraldaObj.qtdFitaAdesiva, 4)
    simulation.elasticoCUT = round(simulation.custoObj.custoElastico * simulation.fraldaObj.qtdElastico, 4)
    simulation.barreiraCUT = round(simulation.custoObj.custoBarreira * simulation.fraldaObj.qtdBarreira, 4)
    simulation.polietileno162CUT = round(simulation.custoObj.custoPolietileno162 * simulation.fraldaObj.qtdPolietileno162, 4)
    simulation.polietileno750CUT = round(simulation.custoObj.custoPolietileno750 * simulation.fraldaObj.qtdPolietileno750, 4)
    simulation.polietileno780CUT = round(simulation.custoObj.custoPolietileno780 * simulation.fraldaObj.qtdPolietileno780, 4)
    simulation.hotMeltCUT = round(simulation.custoObj.custoHotMelt * simulation.fraldaObj.qtdHotMelt, 4)

    simulation.save()
    
    return simulation

def calcular_custo_total_sem_perdas(simulation):
    simulation.fraldaCustoTotalSemPerdas = round(simulation.celuloseVirgemCUT + simulation.gelCUT + simulation.tnt750CUT + simulation.tnt780CUT + simulation.fitaAdesivaCUT + simulation.elasticoCUT + simulation.barreiraCUT + simulation.polietileno750CUT + simulation.polietileno780CUT + simulation.hotMeltCUT, 4)
    
    simulation.save()
    
    return simulation

def calcular_custo_total_com_perdas(simulation):
    simulation.fraldaCustoTotalComPerdas = round(simulation.fraldaCustoTotalSemPerdas * (1 + simulation.fraldaObj.percentPerdas / 100), 4)
    
    simulation.save()
    
    return simulation

def calcular_custo_pacote(simulation):
    simulation.fraldaCustoPacote = round((simulation.fraldaCustoTotalComPerdas * simulation.fraldaObj.qtdPorPacote) + simulation.fraldaObj.precoEmbalagem + simulation.fraldaObj.precoFardoEncarte, 4)
    
    simulation.save()
    
    return simulation

def calcular_custo_unitario_final(simulation):
    simulation.fraldaCUF = round(simulation.fraldaCustoPacote / simulation.fraldaObj.qtdPorPacote, 4)
    
    simulation.save()
    
    return simulation

def calcular_preco_venda(simulation):
    simulation.precoVenda = round(simulation.fraldaCustoPacote / ((100 - simulation.fraldaObj.percentComissao - simulation.fraldaObj.percentImpostos - simulation.fraldaObj.percentFrete - simulation.fraldaObj.percentMargem) / 100), 4)
    
    simulation.save()
    
    return simulation

def calcular_preco_venda_unitario(simulation):
    simulation.precoVendaUnitario = round(simulation.precoVenda / simulation.fraldaObj.qtdPorPacote, 4)
    
    simulation.save()
    
    return simulation
    
def calcular_preco_venda_st(simulation):
    simulation.precoVendaST = round(simulation.precoVenda * (1 + simulation.fraldaObj.percentST / 100), 4)
    
    simulation.save()
    
    return simulation

def calcular_preco_venda_unitario_st(simulation):
    simulation.precoVendaUnitarioST = round(simulation.precoVendaST / simulation.fraldaObj.qtdPorPacote, 4)
    
    simulation.save()
    
    return simulation