salario = int(input('salario'))
if salario <= 1500:
    aliquota = 5
elif salario <= 2500:
    aliquota = 10
elif salario:
    aliquota = 15
  
resultado = salario *(aliquota/100)