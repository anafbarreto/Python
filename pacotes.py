""" Ver pacotes/projetos https://pypi.org/

- Instalar um pacote individualmente
pip install colorama (esse deixa colorido o terminal)

- Instalar uma lista de pacotes
pip install -r requirements.txt 

(o requirements.txt é um arquivo que vamos abrir e escrever dentro dele
o nome do pacote que queremos instalar, nesse caso, colorama. Depois rodas o pip no terminal)"""

# Este arquivo consiste no módulo "modulo_namespace"

# Necessário para fazer o colorama iniciar
colorama.init()

username = 'Dori'

def imprimir(texto, nivel='info'):
    if nivel.lower() == 'info':
        print(colorama.Fore.LIGHTBLUE_EX + f'Info: ', end='')
        print(colorama.Style.RESET_ALL + texto)
    elif nivel.lower() == 'aviso':
        print(colorama.Fore.YELLOW + f'Aviso: ', end='')
        print(colorama.Style.RESET_ALL + texto)
    elif nivel.lower() == 'erro':
        print(colorama.Fore.RED + f'Erro: ', end='')
        print(colorama.Style.RESET_ALL + texto)
    else:
        print(colorama.Fore.RED + 'Erro interno - nível desconhecido de mensagem' + colorama.Style.RESET_ALL)