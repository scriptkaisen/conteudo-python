# Listas -> Vetores -> Arrays
# Varias coisas escritas

# Variáveis? -> Pode guardar 1 unico valor
jogo = "Palworld"

# Lista de jogos favoritos da turma?
jogosFavoritos = [ "Palworld", "Fortnite", 
                  "Smash Karts", "Jedi", "Poki.com", 
                  "Red Dead Redemption 2", "Minecraft" ]

precoDosJogos = [80, 26, 0, 25, 0, 180, 100]

# print(jogo)
# print(jogosFavoritos)

listaDeCelulares = ["Samsung S20FE", "Redmi 15", "Iphone 500K",
                   "Motorola Light 30", "Tablet Da Shopee"]

listaDeAlunos = ["Ingrid", "Pedro Davi", 
                 "Gustavo", "Artur", "Pedro Motta"]

#print(listaDeCelulares)
#print(listaDeAlunos)

#print(listaDeAlunos[1])
#print(listaDeCelulares[1])

#print(listaDeAlunos[4])
#print(listaDeCelulares[4])

elefantinhoVerde = ["Batata Frita", 25, "Jeferson odricandalarai",
                    "Crianças da Malasias", "FullBox", 
                    "Capivara", "Papibaquigrafo", 100]

#print(elefantinhoVerde)

# Adicionar um valor na lista
elefantinhoVerde.append("Sorvete")
#print(elefantinhoVerde)

elefantinhoVerde.append("Anticonstitucionalissimamente")
#print(elefantinhoVerde)

itemRemovido = elefantinhoVerde.pop()
#print(itemRemovido)
#print(elefantinhoVerde)

itemRemovido = elefantinhoVerde.pop()
#print(itemRemovido)
#print(elefantinhoVerde)

itemRemovido = elefantinhoVerde.pop(3)
#print(itemRemovido)
#print(elefantinhoVerde)

elefantinhoVerde.remove("Batata Frita")
# print(elefantinhoVerde)

# Organizar a lista em ordem alfabetica
jogosFavoritos2 = [ "Palworld", "Fortnite", 
                    "Smash Karts", "Jedi", "Poki.com", 
                    "Red Dead Redemption 2", "Minecraft" ]
print(jogosFavoritos2)

jogosFavoritos2.sort()
print(jogosFavoritos2)

jogosFavoritos2.sort(reverse=True)
print(jogosFavoritos2)

# Contar quantos itens tem em uma lista
qtdItens = len(jogosFavoritos2)

# Criar uma lista de numeros
numeros = list(range(1,3))

print(numeros)
print( min(precoDosJogos) )
print( max(precoDosJogos) )

