# Manipulação de Arquivos
# Level do personagem no passe
# 50 Passe
# 00 Passe

# Informação que fica salva constantemente
# Arquivo

level = 10
# abrindo um arquivo com permissão de escrita (w - write) 
arquivo = open("personagem.txt", "w") # abrir
texto = "level = " + str(level) +"\n" # coloquei o texto que eu quero escrever
arquivo.write(texto) # escrevi no arquivo o conteudo da variavel texto
arquivo.write("anteconstitocionalissimamente\n") # escrevendo outra coisa
arquivo.write("pneutramicroscopiosilivulcanoconiotico\n") # escrevendo mais coisas
# tira o arquivo da memoria do computador
arquivo.close() 

# abriu de novo - append ou add
arquivo = open("personagem.txt", "a")
arquivo.write("  Tentando escrever")
arquivo.write("\n Braw Stars com certeza não é melhor que Fortnite")
arquivo.write("\n pabibaquigrafo")
arquivo.write("\n Prefiro sorrir com o Patati")
arquivo.close()

# Ler os aquivos
# abre o arquivo para leitura (r - read)
arquivo = open("personagem.txt", "r") 
conteudo = arquivo.read()
print(conteudo)
print("\nlendo de novo")

# Voltar o cursor para o começo do arquivo
arquivo.seek(41)
conteudo2 = arquivo.read()
print(conteudo2)

print("\nLendo só uma linha")
arquivo.seek(41)
linha = arquivo.readline()
print(linha)

linha2 = arquivo.readline()
print(linha2)

linha3 = arquivo.readline()
print(linha3)
arquivo.close()