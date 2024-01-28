# Criar um arquivo
file = "arquivo.txt"

# Abrir para escrever
arquivo_escrita = open(file, "w")
arquivo_escrita.write("texto a ser escrito")
arquivo_escrita.close()

# Abrir arquivo para leitura
arquivo_leitura = open(file, "r")
leitura = arquivo_leitura.read()
print(leitura)
arquivo_leitura.close()



# Abrir um arquivo binario (0, 1)
arquivo_leitura = open(file, "wb")


