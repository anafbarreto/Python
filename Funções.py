# Criando funções
def saudacao():
    print("Seja bem vinda!")
    print("É um prazer :)")

saudacao()

# Recebendo uma informação
nome= str(input("Oi, qual seu nome?"))
def saudacao(nome):
    print(f"Seja bem vinda! {nome}")
    print("É um prazer :)")
saudacao(nome)

# Função com parametro Default
nome= str(input("Oi, qual seu nome?"))
def saudacao(nome, curso= "Python"):
    print(f"Seja bem vinda! {nome}")
    print(f"É um prazer ter você no nosso curso de {curso} :)")

saudacao(nome) #default não precisa vir na chamada

# Função com retorno
def soma(num1, num2):
   return num1+num2
resultado = soma(5, 5) #inseri os numeros 5 e 5, pq não tem input nesse
print(resultado)

# Exercicio Calculadora
def calculadora(num1, num2, operação="+"):
    if operação == "+":
     return num1+num2
    elif operação == "-":
       return num1-num2

resultado = calculadora(2, 7, "-") #mudando parametro default de + para -
print(resultado)

resultado = calculadora(2, 7)
print(resultado)