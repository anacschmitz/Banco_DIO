import Cliente


class Banco():
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.numero_saque = 0
        self.clientes = []
        self.contas = [1]
        self.cliente = '';

    def validar_senha(self, nome, cpf):

        for user in self.clientes:
            if user.cpf == cpf and user.nome == nome:
                self.cliente = user.nome
                return True
            else:
                return False

    def criar_conta(self):
        conta = Cliente.Conta()
        cliente = Cliente.Usuario()
        retorno = conta.criar_conta(cliente, self.contas)
        self.contas = retorno

    def deposito(self, valor):
        self.saldo += valor
        print(self.saldo)
        self.extrato.append(valor)
        print("Valor depositado com sucesso")

    def saque(self, valor=0):

        if self.numero_saque < 3:
            if self.saldo >= valor:
                self.saldo -= valor
                self.extrato.append("-" + str(valor))
                self.numero_saque += 1
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente! ")
        else:
            print("Máximo de saques diários excedidos!")

    def extrair(self):
        print("------------Extrato DIO Bank------------\nCLiente: {}".format(self.cliente))
        if len(self.extrato) >= 1:
            for i in self.extrato:
                if isinstance(i, str):
                    print("Valor sacado:\n R${:.2f}".format(float(i)))
                    print("-----")
                else:
                    print("Valor depositado:\n R${:.2f}".format(float(i)))
                    print("-----")
            print("Saldo atual: R${:.2f}".format(self.saldo))
        else:
            print("Não foram realizadas movimentações!")
        print("------------Extrato DIO Bank------------")
    def menu(self):
        retorno = input("Qual operação você deseja realizar:\n s - Saque\n e - Extrato\n d - Depósito\n F - Finalizar")
        return retorno


