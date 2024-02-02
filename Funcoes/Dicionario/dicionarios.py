# Criando dicionario
dicionario= {} #dicionario vazio
dicionario= dict() #vazio com função

dicionario= {"nome": "Ana", "idade": 25, "peso" : 86}
print(dicionario)
print(dicionario["nome"]) #mostra a resposta de um parametro especifico

# Adicionando elementos a um dicionario
dicionario["programador"] = True
print(dicionario)

# Alterar uma informação
dicionario["idade"] = 24 #subscreve o dado anterior
print(dicionario)

# Percorrer todos os parametros (chaves)
for variavel in dicionario:
    print(variavel)

# Acessar valor dos parametros (chave)
for chave in dicionario:
    print(chave, dicionario[chave])

# Validar se a chave existe ou não
print("altura" in dicionario)
print("nome" in dicionario)