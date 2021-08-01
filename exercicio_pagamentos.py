#print('{:=^40}'.format('teste diu'))
preco = float(input('Informe o total da compra: '))
print("""
FORMAS DE PAGAMENTO

[ 1 ] PAGAMENTO À VISTA (DINHEIRO)
[ 2 ] PAGAMENTO EM CARTÃO (DÉBITO)
[ 3 ] PAGAMENTO EM CARTÃO (CRÉDITO)
[ 4 ] PAGAMENTO EM CARTÃO (3x)""")


opcao = float(input('Selecione a forma de pagamento: '))

if opcao == 1 : 
    print('O pagamento de {} será feito à vista em dinheiro.'.format(preco))
elif opcao == 2:
    print('O pagamento de {} será feito à vista no cartão de débito.'.format(preco))
elif opcao == 3:
    print('O pagamento de {} será feito em 1x no cartão de crédito.'.format(preco))
elif opcao == 4:
    vezes = int(input('Em quantas vezes deseja parcelar? '))
    if vezes == 2 :
        parcela = preco / vezes
        print('O pagamento de {} será feito em {}x no cartão de crédito, com parcela de {} ao mês.'.format(preco, vezes, parcela))
    elif vezes == 3:
        parcela = preco / vezes
        print('O pagamento de {} será feito em {}x no cartão de crédito, com parcela de {} ao mês.'.format(preco, vezes, parcela))
    else:
        print('Operação não permitida')
else:
    print("""
    Operação não permitida.
    Informe uma opção válida""")
