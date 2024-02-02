# Parecido com o BD
# Da pra fazer um import * e trazer todas as infos, mas não recomendado como uma boa pratica
from modulo_namespaces import username, imprimir 

imprimir(f'Bem vinda, {username}!')

from datetime import datetime
agora = datetime.now()
print(agora)