import re
import sys
from __init__ import Hotel

hotels = ['Lakewood', 'Bridgewood', 'Ridgewood']

#Função para tirar info do input
def FilterLine(line):
    infosHospedagem = []
    aux = line.split(':')
    clienteTipo = aux[0]

    infosHospedagem.append(clienteTipo)
    aux = aux[1]

    r = re.compile(r'\bmon\b | \btues\b | \bwed\b | \bthur\b | \bfri\b | \bsat\b | \bsun\b' , flags=re.I | re.X)
    tmp = r.findall(aux)

    infosHospedagem.append(tmp)

    return infosHospedagem

def Empate(lista_Empate):
    aux = lista_Empate[0]['Classificacao']
    maiorClass = lista_Empate[0]

    for i in range(len(lista_Empate)):
        aux = maiorClass
        if(lista_Empate[i]['Classificacao'] > aux):
            maiorClass = lista_Empate[i]
            aux = maiorClass
    return maiorClass['Nome']

def HotelMaisBarato(hotels, vetorInput):
    lista_Empate = []
    aux = hotels[0].totalValue(vetorInput)
    lista_Empate.append(aux)
    tmp = aux['ValorTotal']
    hotelresultado = aux['Nome']
    for i in range(len(hotels)):
        aux2 = hotels[i].totalValue(vetorInput)
        if(tmp >= aux2['ValorTotal']):
                if (tmp == aux2['ValorTotal']):
                    lista_Empate.append(aux2)
                tmp = aux2['ValorTotal']
                hotelresultado = aux2['Nome']

    if(len(lista_Empate) != 1):
            hotelresultado = Empate(lista_Empate)
    
    if(hotelresultado == 'Lakewood'):
        return 0
    if(hotelresultado == 'Bridgewood'):
        return 1
    else:
        return 2

def get_cheapest_hotel(number):
    cheapest_hotel = hotels[number]
    return cheapest_hotel


def main (argv):
    if (len(argv) != 2):
        sys.exit("Numero Errado de argumentos")
    
    arq = open(str(argv[1]), 'r')

    line = arq.readline()

    arqFiltro = FilterLine(line)
    resp = HotelMaisBarato(hotels, arqFiltro)

    cheapest_hotel = get_cheapest_hotel(resp)

    arq.close()

    print(cheapest_hotel)