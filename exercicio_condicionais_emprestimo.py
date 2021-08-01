casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário do comprador: '))
anos = int(input('Informe em quantos anos será financiado: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
juros = (
print('Para pagar uma casa de R${:.2f} EM {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestacao))
print(juros)
if prestacao <=minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')
