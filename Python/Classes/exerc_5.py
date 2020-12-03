class ContaCorrente:

    def __init__(self, num_conta, nome_corrent, saldo=0):

        self.num_conta = num_conta
        self.nome_corrent = nome_corrent
        self.valor_tot = saldo

    def AlterarNome(self, novo_nome):

        self.nome_corrent = novo_nome

    def Saque(self, valor1=0):

        self.saque_valor = valor1
        self.valor_tot = self.valor_tot - self.saque_valor

    def Deposito(self, valor=0):

        self.deposito_valor = valor
        self.valor_tot = self.valor_tot + self.deposito_valor

    def MostrarInfo(self):

        print(
            f'Número da conta: {self.num_conta}',
            f'\nNome do correntist: {self.nome_corrent}',
            f'\nSaldo: {self.valor_tot}'
        )
