notaum = float(input('Digite a primeira nota: '))
notadois = float(input('Digite a segunda nota: '))
media = (notaum + notadois) /2
print('Sua média foi de {:.1f}'.format(media))
if media >= 7.0:
    print('Sua média foi boa mas pode ser melhor, parabéns!')
else:
    print('Sua média foi péssima')
