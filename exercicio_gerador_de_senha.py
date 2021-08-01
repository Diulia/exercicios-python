#GERADOR DE SENHAS PADRÃO INFRA

from random import choice, random
import string

letras = "abcdefghijklmnopqrstuvwxyz"
letras_maiusculas = letras.upper()
numeros = "0123456789"
simbolos =  "[]{}()*:/,._-"

tamanho = 16
valores = numeros + simbolos + letras + letras_maiusculas
senha = '' 
for i in range(tamanho):
  senha += choice(valores)

print('Gerando senha padrão infra: ')
print(senha)
