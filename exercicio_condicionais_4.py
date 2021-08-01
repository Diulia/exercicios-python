numero = int(input('Escreva um número de 0 a 100: '))
resultado = numero % 2
if resultado == 0 :
    print('O número {} é par'.format(numero))
else :
    print('O número {} é ímpar'.format(numero))
