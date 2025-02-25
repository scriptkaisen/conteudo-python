# Manipular Strings
# O que é string ?
# fio ? Texto ? Linhas ?
# Linha de texto

# Variavel
jogo = "NovA Temporada do Fortnite - nota 10"
print(jogo)

# Contar quantos caracteres tem no texto
qtdCarac = len(jogo)
print(qtdCarac)

# Contar quantas vezes um determinado caractere se repete
qtdAzinho = jogo.count("a")
qtdAzao = jogo.count("A")
print(qtdAzinho + qtdAzao)

# Transformar o texto todo em maiusculo
jogao = jogo.upper()
print(jogao)

# Transformar todo o texto em minusculo
joguinho = jogo.lower()
print(joguinho)

# Trocar todas as letras A por J
jogaoTrocado = jogao.replace("A", "J")
print(jogaoTrocado)
jogaoTrocado = jogao.replace("J", "A")
print(jogaoTrocado)
joguinhoTrocado = joguinho.replace("f", "j")
print(joguinhoTrocado)
robux = jogo.replace("Fortnite", "Robux Gratis")
print(robux)

# Split -> Dividir
# Dividir o texto
sobremesa = "Banana Split não é tão bom assim"
# Espaço separa as palavras - Caractere Delimitador
palavras = sobremesa.split(" ")
print(palavras)
print(palavras[0])
print(palavras[1])
print(palavras[2])
print(palavras[3])
print(palavras[4])
print(palavras[5])
print(palavras[6])
# print(palavras[7]) # -> porque começa no zero

contPalavras = len(palavras)
print(contPalavras)

print(jogo[0])
print(jogo[18])