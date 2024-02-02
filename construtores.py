"""Construtor é um metodo especial. São chamados durante a instanciação de um objeto.
Ou seja quando cria um objeto de uma determinada classe - o construtor é chamado.
"""

# Construtor padrão
class MinhaClasse1:
    def __init__(self): #Definido dentro de uma classe
        print('MinhaClasse1: Chamou o construtor padrão')


class MinhaClasse2:
    pass #Não faz nada, o sistema ignora essa parte aqui

class MinhaClasse3:
    def __init__(self, param):
        print(f'MinhaClasse3: Chamou o construtor parametrizado com o parâmetro {param}')

objeto1 = MinhaClasse1()
objeto2 = MinhaClasse2()
objeto3 = MinhaClasse3('meu-objeto') # parametro que substitui o param na classe 3
