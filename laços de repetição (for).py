
soma = 0

"""
O range é uma faixa de repetição, inicia em 0 e pode receber até 3 parametros:
 ex: range (1, 4) - vai de 1 a 3 **sempre menor que o segundo parametro
O ultimo parametro se chama step, que seria os passos da repetição:
 ex: range (1, 11, 2) - vai contar de 1 à 10, pulando de 2 em 2 (1,3,5,7,9)
"""

for i in range(1, 4):
    nota= float(input(f"Informe sua nota {i}: ")) # o f antes da string, permite incluir uma variavel dentro da mensagem, usando {}

    soma = soma + nota

print (soma / i)