sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo não reconhecido. Por favor insira uma opção válida: ')).strip().upper()[0]
print('Sexo {} registrado.'.format(sexo))