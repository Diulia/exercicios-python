def dar_dicas_de_presente():
  sabe = input('Olá Gutinho lindo amor da minha vida! Já sabe o que me dar de presente de dia dos namorados?' )

  if sabe == "sim" :
    print('Ótimo! Mas não vale eu escolher meu próprio presente')
    return 0
  else: 
    print('Então aqui vai algumas dicas: ')
    print('Chocolate, Lingerie, Maquiagem, Bota')
    presente = input('Digite uma das opções para retornar as dicas ')

  if presente == "chocolate":
    print('Pode ser 5 barra de neugebauer, tá 2,99 no mega')
  elif presente == "lingerie" :
    print('Pode ser qualquer lingerie da Maahina, link da loja no insta https://www.instagram.com/mahinaac/?hl=pt-br')
  elif presente == "maquiagem" :
      print('Pode ser a paleta Soft Nude da Ruby Rose')
  elif presente == "bota":
    print('Pode ser uma botinha de cano e salto baixo, tem que ser número 33')
    return 0

def dar_outra_dica_de_presente():
  naosabe = input('Se precisar de outras dicas digite "Outras" ')
  if naosabe == "outras" :
    print('Você pode comprar o master dos master dos presentes: o anel de pato (Ou uma aliança de verdade, eu não vou reclamar)')
    return 0


dar_dicas_de_presente()
dar_outra_dica_de_presente()





