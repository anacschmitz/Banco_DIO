import math

from Cliente import Usuario
from Funcionalidades import Banco
def menu_principal():
    print("----------------BANCO DIO----------------")
    print("Informe as opções desejadas:\n"
          "[1] - Criar Usuário"
          "[2] - Acessar conta"
          "[3] - Finalizar")
    opcao = int(input("Opção:\n"))
    return opcao

def interacao(opcao:int):
    banco = Banco()
    userAdmin = Usuario("admin", "88-135240", "Rua Joao febronio, 15, Aririu, Palhoça", "00000000000")
    banco.clientes.append(userAdmin)


    if opcao == 1:
        print("|||| INFORME OS DADOS SOLICITADOS E PRESSIONE ENTER")
        cpf = input("Informe o cpf do usuário:\n")
        for user in banco.clientes:
            if user.cpf == cpf:
                break
            else:
                adress = []
                nome = input("Informe o nome do usuário:\n")
                data_nascimento = input("Informe a data de nascimento:\n")
                adress.append(input("Informe o endereço do usuário:\nCep:\n"))
                adress.append(input("Informe nome da rua:\n"))
                adress.append(input("Número da casa:\n"))
                adress.append(input("Bairro:\n"))
                adress.append(input("Cidade:\n"))

                endereco = ", ".join(adress)

                novo_usuario = Usuario(nome, data_nascimento, endereco, cpf)
                banco.clientes.append(novo_usuario)

                print("Usuário Cadastrado com sucesso!")
                opcao = menu_principal()
                interacao(opcao)

    elif opcao == 2:
        cliente = input("Informe o seu nome:\n")
        cpf = input("Informe o seu cpf:\n")

        validacao = banco.validar_senha(cliente, cpf)
        while validacao == False:
            print("Tente novamente:")
            print("__________________")
            cliente = input("Informe o seu nome:")
            cpf = input("Informe o seu cpf:")
            validacao = banco.validar_senha(cliente, cpf)

        answer = '0'
        while answer != '2':
            answer = banco.menu()

            match answer:
                case 's':
                    valor_saque = float(input("Qual o valor que você deseja Sacar?\n R$"))
                    banco.saque(valor=valor_saque)
                case 'd':
                    valor_saque = float(input("Qual o valor você deseja depositar?\nR$"))
                    banco.deposito(valor=valor_saque)
                case 'e':
                    banco.extrair()
                    answer = input("Deseja voltar ao menu inicial?\n [1] RETORNAR\n [2] FINALIZAR")
                    if answer == 1:
                        continue
                    else:
                        answer = '2'
                case 'f':
                    exit()

opcao = menu_principal()
interacao(opcao)


exit()




