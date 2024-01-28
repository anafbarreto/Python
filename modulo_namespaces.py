""" Modulos são locais onde você define os nomes e funções
que quer que fiquem visiveis para o resto do sistema
- Tecnicamente falando, um modulo é um "espaço para declarar nomes", ou seja, um namespace.
- Em um modulo tem variaveis e funções que podemor reutilizar em outro lugares
- Variaveis dentro do namespace são chamadas atributos
Link git https://github.com/WoMakersCode/back-end-python/tree/main/orientacao-a-objetos/1-escopos-e-namespaces"""


username = 'Dori'

def imprimir(texto, nivel='info'):
    if nivel.lower () == 'info' :
        print(f'Info: {texto}')
    elif nivel.lower () == 'aviso' :
         print(f'Aviso: {texto}')
    elif nivel.lower () == 'erro' :
         print(f'Erro: {texto}')
    else:
         print(f'Erro interno - nivel desconhecido')

