"""
Chamado tbm de Mixins
Herdam informações de mais de uma classe base
Muita complexidade, evitar o uso
"""

# Para gerar um arquivo de log
class Logavel:
    def __init__(self):
        self.nome_da_classe = ''
    def logar(self, mensagem):
        print('Mensagem da classe ' + self.nome_da_classe + ': ' + mensagem)

class Conexao:
    def __init__(self):
        self.servidor = ''
    def conectar(self):
        print('Conectando ao banco de dados no servidor ' + self.servidor)
# Teste apenas, mas deveria ter a logica de conexão aqui
        
class MySqlDatabase(Conexao, Logavel):
    def __init__(self):
        super().__init__()
        self.nome_da_classe = 'MySqlDatabase'
        self.servidor = 'MeuServidor'

def framework(objeto):
    if isinstance(objeto, Conexao):
        objeto.conectar()
    if isinstance(objeto, Logavel):
        mensagem = 'Olá mulheres maravilhosas do Bootcamp de Python.'
        objeto.logar(mensagem)

conexao_mysql = MySqlDatabase()
framework(conexao_mysql)