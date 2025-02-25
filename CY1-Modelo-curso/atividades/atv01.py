# Aula 01

# Desafio 1 - Figuras Planas
def FigurasPlanas():
  print("Vamos aprender hoje como calcular a área e o perímetro das seguintes figuras")

  # Quadrado
  print("Quadrado:")
  lado = input("Me fale o valor do tamanho do lado do quadrado: ")
  # O input só recebe textos - string - str
  # converter o texto para numero (float é um numero decimal) 
  # (também poderia converter para int - inteiro) lado = int(lado)
  lado = float(lado)  
  areaQuadrado = lado**2
  print("Para calcular a área do quadrado, eu peguei o valor do lado informado, e elevei ao quadrado.")
  print("O resultado do calculo foi: ")
  print(areaQuadrado)
  print("Para calcular o perímetro, eu preciso pegar o valor do lado e multiplicar por 4.")
  perimetroQuadrado = lado*4
  print("Para o valor informado, o perímtro é de:")
  print(perimetroQuadrado)

  # Retangulo
  print("Retângulo:")
  # área = (base x altura)
  # perimetro = (base*2) + (altura*2)
  baseRet = input("Digite o valor da base: ")
  altRet = input("Digite o valor da altura: ")
  baseRet = float(baseRet)
  altRet = float(altRet)

  areaRet = baseRet * altRet
  perimRet = (baseRet*2) + (altRet*2)

  print("Área do Retangulo é",areaRet)
  print("Perímetro do Retangulo é", perimRet)

  # Triângulo
  print("Triângulo:")
  # área = (base x altura /2)
  # perímetro = lado1 + lado2 + lado3
  baseTri = input("Digite o valor da base: ")
  altTri = input("Digite o valor da altura: ")
  baseTri = float(baseTri)
  altTri = float(altTri)

  areaTri = (baseTri * altTri) / 2

  l1 = input("Digite o valor do lado 1: ")
  l2 = input("Digite o valor do lado 2: ")
  l3 = input("Digite o valor do lado 3: ")

  l1 = float(l1)
  l2 = float(l2)
  l3 = float(l3)

  perimTri = l1 + l2 + l3

  print("Área do Triângulo é",areaTri)
  print("Perímetro do Triângulo é", perimTri) 


  # Losango
  print("Losângo:")
  # área = (diagonal maior * diagonal menor) / 2 
  # perímetro = 4*lado
  diagMaior = input("Digite o valor da diagonal maior: ")
  diagMenor = input("Digite o valor da diagonal menor: ")
  ladoLos = input("Digite o valor do lado: ")

  diagMaior = float(diagMaior)
  diagMenor = float(diagMenor)
  ladoLos = float(ladoLos)

  areaLos = (diagMaior * diagMenor) / 2
  perimLos = ladoLos * 4

  print("Área do Losângo é",areaLos)
  print("Perímetro do Losângo é", perimLos) 


  # Trapézio
  print("Trapézio:")
  # área = ((base maior + base menor) * altura) / 2
  #perímetro = lado1 + lado2 + base maior + base menor

  bMaiorTrap = input("Digite o valor da base maior: ")
  bMenorTrap = input("Digite o valor da base menor: ")
  altTrap = input("Digite o valor da altura: ")
  ld1 = input("Digite o valor do lado 1: ")
  ld2 = input("Digite o valor do lado 2: ")

  bMaiorTrap = float(bMaiorTrap)
  bMenorTrap = float(bMenorTrap)
  altTrap = float(altTrap)
  ld1 = float(ld1)
  ld2 = float(ld2)

  areaTrap = ((bMaiorTrap + bMenorTrap) * altTrap) / 2
  perTrap = ld1 + ld2 + bMaiorTrap + bMenorTrap

  print("Área do Losângo é",areaTrap)
  print("Perímetro do Losângo é", perTrap) 

#FigurasPlanas()

# Desafio 3 - Salário
def desafioSalario():
  numFunc= input("Número do funcionario: ")
  qtdHoras = input("Número de horas trabalhadas: ")
  valorHora= input("Valor por hora: ")

  valorHora = float(valorHora)
  qtdHoras = float(qtdHoras)

  salario = valorHora*qtdHoras

  print("Número =",numFunc)
  print("Salário = ", salario)

#desafioSalario()