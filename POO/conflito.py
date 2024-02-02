from modulo_namespaces import *

# Essa função foi definida no namespace
imprimir(f'Bem vinda, {username}!')
print()


# Essa é uma função desenvolvida com os mesmos nomes
def imprimir(texto):
    print(texto)
imprimir(f'Bem vinda, {username}!')

"""O python vai executar linha por linha e retornar duas vezes as mesmas informações
esse é o risco de usar o import com *, quando usamos bibliotecas de terceiros
não tem como garantir todos os nomes, por isso melhor trazer só o que precisa"""

