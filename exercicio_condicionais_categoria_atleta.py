from datetime import date
datahoje = date.today().year
nascimento = int(input('Qual seu ano de nascimento? '))
idade = datahoje - nascimento

if idade > 25:
    print('Você nasceu em {} e está na categoria \033[1;30;41mMaster.\33'.format(nascimento))
elif idade >= 19 and idade <= 24:
    print('Você nasceu em {} e está na categoria \033[1;30;44mSênior.\033'.format(nascimento))
elif idade >= 14 and idade < 19:
    print('Você nasceu em {} e está na categoria \033[1;35;43mJúnior.\033'.format(nascimento))
elif idade >= 9 and idade < 13:
    print('Você nasceu em {} e está na categoria \033[1;30;42mInfantil.\033'.format(nascimento))
elif idade <= 9:
    print('Você nasceu em {} e está na categoria \33[4;33;43mMirim.\033'.format(nascimento))
    
