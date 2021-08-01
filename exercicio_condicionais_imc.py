peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)
print('Sei IMC é de {}.'.format(imc))
if imc <= 18.9:
     print('Você está abaixo do peso')
elif imc >= 19 and imc < 24.9 :
   print('Seu peso está normal')
elif imc >= 25 and imc < 30 :
    print('Você está com sobrepeso')
else:
    print('Você está obeso')
