# Laço de Repetição

# O que é?
# Sempre -> Scratch
# Repita até que -> Scratch
# Repita 10 vezes -> Scratch

# Condição eterna
# Enquanto uma condição for verdade
'''
while (True):
  print("One Piece is Real!")  

'''

# Condição para pausa
rodar = True
# Roda enquanto uma condição for verdadeira
'''
while (rodar == True):
  print("A capithanos está vindo!")
  resposta = input("Ela já chegou? s - Sim | n - Não \n")
  if(resposta == "s" or resposta == "S"):
    rodar = False
  else:
    rodar = True

print("Ela chegou!!")
'''

'''
listaCapivaras = ["Capivaras de Cruzeiro", "Capivaras do Fornai", "Capivaras Youtubers", "Capivara IA Cover"]

# Repita x Vezes
# Para
for x in range(0,4):
  print(x)
  print(listaCapivaras[x])

print("Percorrendo pela lista sem Range")
for item in listaCapivaras:
  print(item)
'''

'''
Faça um programa que recebe um número de 1 a 10 e imprime a tabuada desse número.
'''
# input recebe um string -> Texto
numero = input("Digite um numero de 1 a 10:\n")
# Converter o texto (string) para inteiro
numero = int(numero)

for x in range(1,11):
  print(numero,"x", x ,"=", numero*x)



