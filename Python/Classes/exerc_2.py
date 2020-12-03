class Quadrado:

    def __init__(self, lado=1):

        self.lado = lado

    def MudarLado(self, lado2=1):

        self.lado = lado2

    def RetornarLado(self):

        print(f'O valor do lado do quadrado é {self.lado}')

    def calArea(self):

        area = self.lado * self.lado
        print(f'A área do quadrado é {area}')
