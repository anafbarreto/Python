# Definição da classe
class Carro: # Convenção para nomes de classes: PascalCasing
    def __init__(self):
        self.ligado = False
        self.cor = "Chumbo"
        self.modelo = "Sedan"
        self.velocidade = 0
        self.velocidade_min = 1
        self.velocidade_max = 200
        
    
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
         
    def acelera(self):
        if not self.ligado:
            return

        if self.velocidade < self.velocidade_max:
            self.velocidade += 5

    def desacelera(self):
        if not self.ligado:
            return

        if self.velocidade > self.velocidade_min:
            self.velocidade -= 5

    def __str__(self) -> str: # Para exibir as informações em string no resultado
        return f'Carro - ligado {self.ligado} - Cor {self.cor} - Modelo {self.modelo} - Velocidade {self.velocidade}'

# Criando instâncias da class carro
meu_carro = Carro()


# Faça o carro andar
meu_carro.ligar()
print('O carro está ligado? {}'.format(meu_carro.ligado))


for i in range(5):
    meu_carro.acelera()

print('Velocidade: {}'.format(meu_carro.velocidade))
print()

# Faça o carro parar
meu_carro.ligar()
print('O carro está ligado? {}'.format(meu_carro.ligado))


for i in range(5):
    meu_carro.desacelera()

print('Velocidade: {}'.format(meu_carro.velocidade))
print()
