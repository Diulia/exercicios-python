from datetime import date
datahoje = date.today().year
nascimento = int(input('Qual o ano em que você nasceu? '))
idade = datahoje - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, datahoje))


if idade == 18 :
    print('Você deve se alistar esse ano')
elif idade < 18:
    diferenca = 18 - idade
    print('Você ainda não tem idade para se alistar. Seu alistamento será em {} anos.'.format(diferenca))
elif idade > 18:
    diferenca = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(diferenca))
    
