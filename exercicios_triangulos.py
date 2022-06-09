a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
  if a == b and a == c:
   print('triângulo equilatero')
  elif a == b or b == c or a == c:
      print('triângulo isosceles') 
  else:
    print("triângulo escaleno") 
else:
    print('não é triângulo')