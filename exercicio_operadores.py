#EXERCÍCIO DE FIXAÇÃO 01 OPERADORES

#FLOAT É USADO PARA DEFINIR QUE O NÚMERO NÃO É UM INTEIRO
numeroum = float (input('Digite o primeiro número: '))
numerodois = float (input('Digite o segundo número: '))

#OPERAÇÕES SIMPLES
soma = numeroum+numerodois
divisao = numeroum+numerodois
subtracao = numeroum-numerodois
potencia = numeroum**numerodois

#CONDIÇÃO DA DIVISÃO SE NUMERO2 FOR IGUAL A 0 ENTÃO VAI SER 0 SENÃO É CALCULADO NORMALMENTE
if numerodois <=0 : 
	divisao =0
else : 
	divisao = numeroum/numerodois

print ("O resultado da soma dos números é", soma, "e a diferença é", subtracao)
print ("o resultado da divisão é", divisao, "e a potencia é: ", potencia)
