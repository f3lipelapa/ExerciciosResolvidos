class Pessoa:

    def __init__(self, nome, idade, peso, altura):

        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Envelhecer(self, nova_idade):

        cont = self.idade
        while cont < nova_idade:
            self.altura += 0.05
            cont += 1
        self.idade = nova_idade

    def Crescer(self, nova_altura):

        self.altura = self.nova_altura

    def Engordar(self, alto_peso):

        self.peso = alto_peso

    def Emagrecer(self, baixo_peso):

        self.peso = baixo_peso

    def MostrarDados(self):

        print(
            f'Nome: {self.nome}',
            f'\nIdade: {self.idade} anos',
            f'\nPeso: {self.peso} Kg',
            f'\nAltura: {self.altura:.2f} metros'
        )
