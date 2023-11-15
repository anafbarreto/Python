# Conversão de tipo
idade = "26"
peso = "76"

# se você quiser concatenar é só fazer 
print(idade + peso)

idade_numerica = int(idade)
print(idade_numerica)

print(type(idade), type(idade_numerica))

""" tudo que entrar no input é str
precisa converter as informações """

altura = float(input("informe sua altura: "))
