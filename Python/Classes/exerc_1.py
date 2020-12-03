class Bola:

    def __init__(self, cor='', circ=1, mat=''):

        self.cor = cor
        self.circunferencia = circ
        self.material = mat

    def trocaCor(self, CorNova=''):

        self.cor = CorNova

    def mostraCor(self):

        print(f'A cor da bola é {self.cor}')
        
