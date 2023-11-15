# Controle de fluxo 

# Validando maioridade
idade = int(input("Qual sua idade? "))

if idade >= 18: # os dois : é equivalente ao then
    print("Bem vindo!")
else: print("Menor de idade!") 

# Aprovado ou reprovado
nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
nota3 = float(input("Insira a nota 3: "))

media = ((nota1+nota2+nota3)/3)

if media >= 6:
    print("Sua média é:", media, "- Aprovada!")
else: print("Reprovada!")

# Para limitar as casas decimais da média
# round(variavel que quer limitar, qtde de casas depois da ,)
if media >= 6:
    print("Sua média é:", round(media,2),"- Aprovada!")
else: print("Reprovada!")

# Python não tem else if, usar elif
if media >= 7:
    print("Sua média é:", round(media,2),"- Aprovada!")
elif media >= 5 and media < 7:
    print("Sua média é:", round(media,2),"- Recuperação!")
else: print("Reprovada!")

""" 
Para duas condições usar and = e
Para uma ou outra usar or =
Atenção a identação

"""