# Estruturas Condicionais

# Condição:
# separa uma coisa da outra
# algo q vc faz pra fazer outra coisa
# Reação em cadeia

# condição: se vc clicar 100 vezes
# ação:     sua velocidade é 100

nClick = 100
velocidade = 0

# TODA CONDIÇÃO PODE SER VERDADEIRA (1) OU FALSA (0)
if (nClick >= 100):
  # verdadeira
  velocidade = 100
else:
  # falsa
  velocidade = 10

#print(velocidade)
'''
  Se clicar 200 vezes ou mais
  velocidade 200
  
  Se clicar 100 vezes ou mais
  velocidade 100
  
  Se clicar menos de 100 vezes
  velocidade 10
'''

nClick = 240
velocidade = 0
if (nClick >= 100 and nClick < 200):
  velocidade = 100
elif (nClick >= 200):
  velocidade = 200
else:
  velocidade = 10

print(velocidade)
'''
  Loja do jogo
  Gold, Diamond
  
  Comprar Bau no jogo
  1000 Gold ou 5 Diamonds  
'''
gold = 15
diamond = 6

if (gold >= 1000 or diamond > 5):
  print("Sou Rica! Posso abrir baú!!!")
  
else:
  print("Sou pobre, me de gold!")
