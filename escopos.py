""" Escopo de variaveis:
Variaveis declaradas dentro de uma função, não podem ser acessadas fora dela.
Variaveis declaradas fora de qualquer função são chamadas de globais
"""

bebida = 'refrigerante'

def cardapio():
    comida = 'hamburguer'
    bebida = 'suco' ## aqui a variavel bebida recebe a info suco
    print('comida:', comida)
    print('bebida:', bebida)

cardapio()
print('bebida:', bebida) # aqui ela ainda vai exibir refrigerante, pq esta fora da função


# incluindo a linha 21 (global bebida), a função vai alterar a variavel existente
# ao inves de criar uma nova
def cardapio():
    global bebida
    comida = 'hamburguer'
    bebida = 'suco' # bebida recebe suco
    print('comida:', comida)
    print('bebida:', bebida)

cardapio()
print('bebida:', bebida)  # bebida recebe suco
