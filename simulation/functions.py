def calcular_custo_unitario_total_por_componente(simulacao):
    simulacao.celuloseVirgemCUT = round(simulacao.custoObj.custoCeluloseVirgem * simulacao.fraldaObj.qtdCeluloseVirgem, 4)
    simulacao.gelCUT = round(simulacao.custoObj.custoGel * simulacao.fraldaObj.qtdGel, 4)
    simulacao.tnt162CUT = round(simulacao.custoObj.custoTnt162 * simulacao.fraldaObj.qtdTnt162, 4)
    simulacao.tnt750CUT = round(simulacao.custoObj.custoTnt750 * simulacao.fraldaObj.qtdTnt750, 4)
    simulacao.tnt780CUT = round(simulacao.custoObj.custoTnt780 * simulacao.fraldaObj.qtdTnt780, 4)
    simulacao.fitaAdesivaCUT = round(simulacao.custoObj.custoFitaAdesiva * simulacao.fraldaObj.qtdFitaAdesiva, 4)
    simulacao.elasticoCUT = round(simulacao.custoObj.custoElastico * simulacao.fraldaObj.qtdElastico, 4)
    simulacao.barreiraCUT = round(simulacao.custoObj.custoBarreira * simulacao.fraldaObj.qtdBarreira, 4)
    simulacao.polietileno162CUT = round(simulacao.custoObj.custoPolietileno162 * simulacao.fraldaObj.qtdPolietileno162, 4)
    simulacao.polietileno750CUT = round(simulacao.custoObj.custoPolietileno750 * simulacao.fraldaObj.qtdPolietileno750, 4)
    simulacao.polietileno780CUT = round(simulacao.custoObj.custoPolietileno780 * simulacao.fraldaObj.qtdPolietileno780, 4)
    simulacao.hotMeltCUT = round(simulacao.custoObj.custoHotMelt * simulacao.fraldaObj.qtdHotMelt, 4)

    simulacao.save()
    
    return simulacao

def calcular_custo_total_sem_perdas(simulacao):
    simulacao.fraldaCustoTotalSemPerdas = round(simulacao.celuloseVirgemCUT + simulacao.gelCUT + simulacao.tnt750CUT + simulacao.tnt780CUT + simulacao.fitaAdesivaCUT + simulacao.elasticoCUT + simulacao.barreiraCUT + simulacao.polietileno750CUT + simulacao.polietileno780CUT + simulacao.hotMeltCUT, 4)
    
    simulacao.save()
    
    return simulacao

def calcular_custo_total_com_perdas(simulacao):
    simulacao.fraldaCustoTotalComPerdas = round(simulacao.fraldaCustoTotalSemPerdas * (1 + simulacao.fraldaObj.percentPerdas / 100), 4)
    
    simulacao.save()
    
    return simulacao

def calcular_custo_pacote(simulacao):
    simulacao.fraldaCustoPacote = round((simulacao.fraldaCustoTotalComPerdas * simulacao.fraldaObj.qtdPorPacote) + simulacao.fraldaObj.precoEmbalagem + simulacao.fraldaObj.precoFardoEncarte, 4)
    
    simulacao.save()
    
    return simulacao

def calcular_custo_unitario_final(simulacao):
    simulacao.fraldaCUF = round(simulacao.fraldaCustoPacote / simulacao.fraldaObj.qtdPorPacote, 4)
    
    simulacao.save()
    
    return simulacao

def calcular_preco_venda(simulacao):
    simulacao.precoVenda = round(simulacao.fraldaCustoPacote / ((100 - simulacao.fraldaObj.percentComissao - simulacao.fraldaObj.percentImpostos - simulacao.fraldaObj.percentFrete - simulacao.fraldaObj.percentMargem) / 100), 4)
    
    simulacao.save()
    
    return simulacao

def calcular_preco_venda_unitario(simulacao):
    simulacao.precoVendaUnitario = round(simulacao.precoVenda / simulacao.fraldaObj.qtdPorPacote, 4)
    
    simulacao.save()
    
    return simulacao
    
def calcular_preco_venda_st(simulacao):
    simulacao.precoVendaST = round(simulacao.precoVenda * (1 + simulacao.fraldaObj.percentST / 100), 4)
    
    simulacao.save()
    
    return simulacao

def calcular_preco_venda_unitario_st(simulacao):
    simulacao.precoVendaUnitarioST = round(simulacao.precoVendaST / simulacao.fraldaObj.qtdPorPacote, 4)
    
    simulacao.save()
    
    return simulacao