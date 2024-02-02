# Antes das listas
nota1 = 7
nota2 = 8
nota3 = 9.2

# Com as listas
notas = [7, 8, 9.2]

# Criando listas
lista = [] #lista vazia
lista = list() #lista vazia com função
lista = [25, "ana", 86.6, False] #lista aceita varios tipos de dados
lista_de_listas = [10, [1, 2, 3,["ana"]]]

# Indexação
lista = [25, "ana", 86.6, False]

print(lista[1]) #2° posição da lista
print(lista[0]) #lembrando que essa é a primeira posição
print(lista[2]) #3° posição da lista

print(lista[-1]) #ultimo item da lista
print(lista[-2]) #penultimo e assim até acabar os elementos

# Slices (fatiamento de listas)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[0:3]) #pega as posições 0, 1 e 2 da lista ** sempre -1 do valor final do parametro
print(lista[2:]) #começa na posição dois da lista (numero 3 nesse caso) e vai até acabar
print(lista[0:10:2]) #pulando de 2 em 2, igual ao range

# Interações com o FOR
    # Com elementos da propria lista
for elemento in lista:
    print(elemento) #percorre um por um

    # Com os indices da lista
print("comprimento da lista =", len(lista), "elementos") #conta os elementos

for i in range(len(lista)): #aqui o len(lista) funciona como um parametro para o range
    print(i)
