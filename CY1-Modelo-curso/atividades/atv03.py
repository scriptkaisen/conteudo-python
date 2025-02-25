# Aula 03
# Desafio 01

def Desafio01p1():
  valor = input("Digite um valor:")
  valor = int(valor)  
  vetor = [valor]
  
  print(vetor[0])
  vetor.append(vetor[0]*2)

  print(vetor[1])
  vetor.append(vetor[1]*2)

  print(vetor[2])
  vetor.append(vetor[2]*2)

  print(vetor[3])
  vetor.append(vetor[3]*2)

  print(vetor[4])
  vetor.append(vetor[4]*2)

  print(vetor[5])
  vetor.append(vetor[5]*2)

  print(vetor[6])
  vetor.append(vetor[6]*2)

  print(vetor[7])
  vetor.append(vetor[7]*2)

  print(vetor[8])
  vetor.append(vetor[8]*2)

  print(vetor[9])

def Desafio01p2():
  valor = input("Digite um valor:")
  valor = int(valor)    
  vetorLaco = [valor]

  for i in range(999999999999999999999999999999):
    print("[",i,"]:",vetorLaco[i])
    vetorLaco.append(vetorLaco[i]*2)

  print("[",len(vetorLaco)-1,"]:",vetorLaco[len(vetorLaco)-1])

