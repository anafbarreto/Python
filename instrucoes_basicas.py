# print: é um comando que exibe mensagem ou resultado
print("Hello world") 

""" Tipos de variaveis
1. int: numeros inteiros;
2. float:  numeros reais - com partes decimais;
3. str: (string) cadeia de caracteres - dados de texto;
4. bool: booleanos - true or false """

idade = 25
altura = 1.77
nome = "Ana Carolina"
estudando = True # Maiusculo e minusculo fazem diferença

# imprimir tipo das variaveis
print (type (idade))
print (type (altura))
print (type (nome))
print (type (estudando))

# input: função para entrada de informações
# o padrão de entrada python é string
linguagem = input("Qual linguagem de programação está estudando? ")

print("A linguagem que você está estudando é:",linguagem)

# Imprimindo varias infos
print(nome, idade, linguagem)

# Imprimindo varias infos separadas por virgula
print(nome,",", idade,",", linguagem)

