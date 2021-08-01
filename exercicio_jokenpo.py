from random import randint
item = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
print('A máquina escolheu {}.'.format(maquina))
print("""
ESCOLHA UM DOS ITENS:

[0] PEDRA
[1] PAPEL
[2] TESOURA
""")
jogador = int(input('Informe a sua escolha: '))
print('-=' * 12)
print('O computador jogou {}. '.format(item[maquina]))
print('O jogador jogou {}. '.format(item[jogador]))
print('-=' * 12)

if maquina == 0 : #PEDRA
    if jogador == 0 :
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCEU')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU')
    else:
        print('Jogada inválida')
    
elif maquina == 1: #PAPEL
    if jogador == 0 :
        print('O COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O JOGADOR VENCEU')

elif maquina == 2: #TESOURA
    if jogador == 0 :
        print('O JOGADOR VENCEU')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
else:
    print('Jogada inválida')
