class Usuario:
    def __init__(self, nome, data_nascimento, endereco, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.cpf = cpf

class Conta:
    def __init__(self, cliente: Usuario, contas:list):
        self.agencia = "0001"
        self.numero_conta = contas[len(contas)] + 1
        contas.append(self.numero_conta)
        return contas


