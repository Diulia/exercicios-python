notaum = float(input('Primeira nota: '))
notadois = float(input('Segunda nota: '))
media = (notaum + notadois) / 2
if media >= 7 :
    print('A sua média é de {:.2f} e você está \033[1;32mAPROVADO\033.'.format(media))
elif media < 6:
    print('A sua média é de {:.2f} e você está \033[1;30;41mREPROVADO\033.'.format(media))
elif media >= 6 and media < 7:
    print('A sua média é de {:.2f} e você está em \033[1;33mRECUPERAÇÃO\033.'.format(media))
    
