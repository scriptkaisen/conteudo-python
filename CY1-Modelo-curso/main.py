listaDeJogos = ["fortnite", "roblox", "valorant", "rocket league", "the isle"]
print (listaDeJogos)
listaPrecos = [0, 0, 0, 35, 40]
print (listaPrecos)
print ("qual jogo deseja consultar?")
jogo = input()

if jogo in listaDeJogos:
  print ("o preço do jogo é", listaPrecos[listaDeJogos.index(jogo)])
else:
  print("seu jogo não esta disponivel")


  
