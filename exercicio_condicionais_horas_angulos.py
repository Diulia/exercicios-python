#HORAS EM ÂNGULOS

hora_grau = 30
minuto_grau = 6
hora_recebe = int(input("Insira as horas: "))
minuto_recebe = int(input("Insira os minutos: "))

grau_um = hora_recebe * hora_grau
grau_dois = minuto_recebe * minuto_grau

angulo = grau_um - grau_dois
angulo = abs(angulo)
angulo_inverso = 360 - angulo

if angulo < angulo_inverso :
    print(str(angulo)+"é o menor ângulo")
elif angulo > angulo_inverso:
    print(str(angulo_inverso)+"é o menor ângulo")
else :
    print("Os ângulos são iguais")
    
    
    

                                          

