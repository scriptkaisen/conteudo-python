# Dicionarios, Tuplas e Sets
# Tipos de dados diferentes
# Estutura de dados diferentes

# Tuplas - Dicionários
# Tuplas?
# Tuplas são iguais as Listas
# Mas não podem ser modificadas

lista = ["item1", "item2", "item3"]
print(lista)
lista.append("item4")
print(lista)

tupla = ("item1", "item2", "item3")
print(tupla)

lista[0] = "item4"
print(lista[0])

print(tupla[0])


# Sets - Conjuntos
# Listas -> MAS não permite repetições
# Listas que não permitem valores repetidos

listaSet = set()
listaSet.add("item1")
listaSet.add("item1")
listaSet.add("item2")
listaSet.add("item2")
listaSet.add("item3")
listaSet.add("item3")
print(listaSet)


# Dicionários
# Palavra - significado
# Keys - value
dicionario = {
    "key1":"value1",
    "key2": "value2",
    "key3": "value3"
}

print(dicionario)
print(dicionario.keys())
print(dicionario.values())
print(dicionario["Pinguin"])

# Dicionários
listaDeCompras = {
  "Banana": 12, 
  "Batata": 20, 
  "Barra de chocolate": 5
}

listaDeNumeros = {
  1: "Um", 
  2: "Dois", 
  3: "Cinco"
}

print(listaDeCompras["Batata"])
print(listaDeNumeros[3])

