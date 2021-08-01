#exercicio 08 - conversor de medidas
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm, {:.0f}dm, {:.0f}dam, {.:0f}hm, {:.0f}km'.format(medida, cm, mm, dm, dam, hm, km))
