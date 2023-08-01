import math

from Funcionalidades import Banco


print("----------------BANCO DIO----------------")
cliente = input("Informe o seu nome:")
senha = input("Informe a sua senha:")

banco = Banco(cliente, senha)

while banco.validar_senha() == False:
    print("Tente novamente:")
    print("__________________")
    cliente = input("Informe o seu nome:")
    senha = input("Informe a sua senha:")
    banco = Banco(cliente, senha)

answer = '0'
while answer != '2':
    opcao = banco.menu()

    match opcao:
        case 's':
            valor = float(input("Qual o valor que você deseja Sacar?\n R$"))
            banco.saque(valor)
        case 'd':
            valor = float(input("Qual o valor você deseja depositar?\nR$"))
            banco.deposito(valor)
        case 'e':
            banco.extrair()
            answer = input("Deseja voltar ao menu inicial?\n [1] RETORNAR\n[2] FINALIZAR")
            if answer == '1':
                continue
            elif answer == '2':
                break
                print("Fim!")
