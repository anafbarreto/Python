# Metodo de listas
lista = [1, 3, 12, 8, 2]

# Append - adiciona elementos (sempre no final)
lista.append(3) #inclui o 3 como ULTIMO elemento
print(lista)

# Insert - adiciona elementos (você escolhe a posição)
lista.insert(2, 10) #inclui na posição 2, o numero 10
print(lista)

# Extend - Junta listas
lista2 = [2, 4, 6]
lista.extend(lista2) #lista2 serão os ultimos elementos da lista
print(lista)

# POP - elimina elementos
lista.pop() #apaga o ultimo
lista.pop(2) #apaga elemento na 2° posição
print(lista)

# Remove - elimina o elemento (numero mesmo)
lista.remove(1) #exclui o numero 1, numero e não posição
print(lista) #se tiver mais de 1, precisa repetir e repetir até apagar todos

# Count - contagem
lista.count(2)
print("a qtde de numeros 2 na lista é:", lista.count(2))

# Index - fala o indice de um elemento na lista
print("o numero 12 está na posição:", lista.index(12))

# Sort - ordenação
lista.sort() #ordem crescente
print(lista)
lista.reverse() #lista.sort(reverse = True) também funciona
print(lista)
lista.sort(reverse = True)
print(lista)

# FUNÇÕES PARA LISTAS
    # 1. len - saber quantos elementos tem na lista
print(len(lista))

    # 2. sum - soma dos elementos
print(sum(lista))

    # 3. max - maior valor
print(max(lista))

    # 4. min - menor valor
print(min(lista))
