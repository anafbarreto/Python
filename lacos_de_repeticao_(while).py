
num_sorteado = 15
num_escolhido = int(input("Informe um numero de 1 a 20: "))

while num_escolhido != num_sorteado:
    print("Você errou, tente novamente")
    num_escolhido = int(input("Informe um numero de 1 a 20: "))

print("Parabéns! Você acertou!")