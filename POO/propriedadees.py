"""Se um usuário da classe quiser acessar os membros protegidos e privados, ele tem como fazer isso, mas vai estar quebrando as regras de encapsulamento, que de novo, são definidas por convenções nos nomes das variáveis.
Existe uma forma de controlar um pouco melhor como um usuário vai acessar os atributos de uma classe, que é através de propriedades.
Propriedades podem ser definidas pelo uso do decorator @property. Esse decorator cria o método getter da propriedade.
Para alterar o valor de uma propriedade externamente à classe, é preciso criar o método setter."""




class Quadrado:
  def __init__(self, medida):
    self.altura = medida
    self.largura = medida

  @property
  def altura(self):
    return self.__medida

  @altura.setter
  def altura(self, valor):
    # executa algum tipo de validação
    self.__medida = valor

  @property
  def largura(self):
    return self.__medida

  @largura.setter
  def largura(self, valor):
    # executa algum tipo de validação
    self.__medida = valor

  def area(self):
    return self.largura * self.altura