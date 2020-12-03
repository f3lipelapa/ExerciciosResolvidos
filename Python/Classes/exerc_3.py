class Retangulo:

    def __init__(self, comp, larg):

        self.comprimento = comp
        self.largura = larg

    def MudarMedidas(self, comp2, larg2):

        self.comprimento = comp2
        self.largura = larg2

    def RetornarValores(self):

        return self.comprimento, self.largura

    def calArea(self):

        area = self.comprimento * self.largura
        return area

    def calPerimetro(self):

        perimetro = (self.comprimento * 2) + (self.largura * 2)
        return perimetro


# Entrada - dados que o cliente vai colocar
while True:
    try:
        compr_local = float(input('Digite o comprimento do local: '))
        largu_local = float(input('Digite a largura do local: '))
    except (ValueError):
        print('Digite os valores novamente.')
    else:
        local = Retangulo(compr_local, largu_local)
        break
print('\n')
while True:
    try:
        compr_piso = float(input('Digite o comprimento do piso: '))
        largu_piso = float(input('Digite a largura do piso: '))
    except (ValueError):
        print('Digite os valores novamente.')
    else:
        piso = Retangulo(compr_piso, largu_piso)
        break

# Respostas - o que o cliente vai receber
valor_local = local.RetornarValores()
valor_piso = piso.RetornarValores()
print(
    f'\nOs valore do local são: {valor_local}',
    f'\nOs valores do piso são: {valor_piso}'
)
quant_piso = local.calArea() / piso.calArea()
print(f'A quantidade de pisos necessários é {quant_piso}')

quant_roda = local.calPerimetro() / compr_piso
print(f'A quantidade de rodapés necessários é {quant_roda}')
