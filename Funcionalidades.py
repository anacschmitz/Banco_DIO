class Banco():
    def __init__(self, nome_cliente, senha):
        self.conta = "001-01"
        self.agencia = "1015-10"
        self.nome_cliente = nome_cliente
        self.senha = senha
        self.saldo = 0.0
        self.extrato = []

    def validar_senha(self):
        senha_cadastrada = "12345"
        cliente_cadastrado = "Ana"

        if self.senha == senha_cadastrada and self.nome_cliente == cliente_cadastrado:
            return True
        else:
            return False

    def deposito(self, valor):
        self.saldo =+ valor
        print(self.saldo)
        self.extrato.append(valor)
        print("Valor depositado com sucesso")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo =- valor
            self.extrato.append("-" + str(valor))
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente! ")

    def extrair(self):
        print("------------Extrato DIO Bank------------\nCLiente: {}".format(self.nome_cliente))
        for i in self.extrato:
            if isinstance(i, str):
                print("Valor sacado:\n R${:.2f}".format(float(i)))
                print("-----")
            else:
                print("Valor depositado:\n R${:.2f}".format(float(i)))
                print("-----")
        print("------------Extrato DIO Bank------------")

    def menu(self):
        retorno = input("Qual operação você deseja realizar:\n s - Saque\n e - Extrato\n d - Depósito")
        return retorno


