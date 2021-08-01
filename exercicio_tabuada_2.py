numero = int(input('Digite um número para ver sua tabuada: '))
for num in range(1, 11):
    print('{} x {:2} = {}.'.format(num, numero, numero*num))