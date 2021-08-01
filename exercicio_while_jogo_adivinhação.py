from random import randint
computador = randint (0, 10)
print('Adivinhe um número de 1 a 10')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o número? '))
    palpite += 1
    if jogador == computador:
        acertou =  True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
print('Acertou com {} palpites! '.format(palpite))
