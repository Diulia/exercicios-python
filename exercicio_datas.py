#Biblioteca de datas
from datetime import datetime

#Formato de data
date_format = "%d/%m/%Y"
#Data inicial
datainicial = datetime.strptime (input('Data inicial: '), date_format)
#Data final
datafinal = datetime.strptime (input('Data final: '), date_format)
# Realizamos o calculo da quantidade de dias
dias = ((datafinal - datainicial).days)

print('Quantos dias faltam para finalmente voltar para PF? ', dias, 'dias')
