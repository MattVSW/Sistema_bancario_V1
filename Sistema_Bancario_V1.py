menu = """
O que deseja realizar?

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato= ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")

        deposito = float(input("quanto deseja depositar: R$"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito R${deposito: .2f}\n"
            print("Deposito feito com sucesso")
        else:
            print("Não é possivel realizar essa operação!")

    elif opcao == "s":
        print("Sacar")
        saque = float(input("Qual valor deseja sacar: R$"))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if saque <= 0:
            print("Operação invalida, valor invalido para saque.")

        elif excedeu_saldo:
            print("Operação invalida, saldo insuficiente.")
        
        elif excedeu_limite:
            print("Operação invalida, valor limite excedido.")
        
        elif excedeu_saques:
            print("Operação invalida, excedeu quantidade de saques diários.")

        elif saque > 0:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque R${saque:.2f}\n"
            print("Saque realizado, retire o dinheiro na boca do caixa.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema bancário, tenha um otimo dia!!!")
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")