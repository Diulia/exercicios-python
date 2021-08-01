velocidade = float(input('Qual a velocidade em que você está dirigindo? '))
if velocidade > 80:
    print('Você foi multado! Excedeu o limite de velocidade permitido (O limite é de 80km/h)')
    multa = (velocidade-80) * 15
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tudo bem, dirija com cuidado')

    
