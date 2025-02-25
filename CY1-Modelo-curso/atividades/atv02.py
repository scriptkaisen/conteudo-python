# Aula 02 
# Desafio 1 - Conta vogais e espaços
def contVogais():
  frase = input("Digite uma frase bem legal:\n")

  qtdEsp = frase.count(" ")
  qtdA = frase.count("a") + frase.count("A")
  qtdE = frase.count("e") + frase.count("E")
  qtdI = frase.count("i") + frase.count("I")
  qtdO = frase.count("o") + frase.count("O")
  qtdU = frase.count("u") + frase.count("U")

  print("Quantidade de espaços:",qtdEsp)
  print("Quantidade de A:",qtdA)
  print("Quantidade de E:",qtdE)
  print("Quantidade de I:",qtdI)
  print("Quantidade de O:",qtdO)
  print("Quantidade de U:",qtdU)

# contVogais()

def exibeNomes():
  # Ingrid Liana Leite Silva
  nomeCompleto = input("Digite seu nome completo:\n")

  nomes = nomeCompleto.split(" ")
  primeiroNome = nomes[0]
  ultimoNome = nomes[ len(nomes)-1 ]

  sobreNomeCompleto = nomeCompleto.replace(primeiroNome+" ", "")

  print("1 - Seu primeiro nome é: ")  
  print(primeiroNome)  

  print("2 - Seu sobre nome completo é: ")
  print(sobreNomeCompleto)

  print("3 - Seu ultimo nome é: ")
  print(ultimoNome)

# exibeNomes()