saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """ 
Depositar (d)
Sacar (s)
Extrato (e)
Fechar (f)
"""

while True: 
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do seu depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de: ---> {valor:.2f}\n"
        else:
            print("Erro! Valor de depóisito inválido")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do seu saque: "))

        if valor > saldo:
            print("Valor do saque excedeu o saldo atual!")

        elif valor > limite:
            print("O valor do saque ultrapassou o limite máximo de R$500")

        elif numero_saques >= LIMITE_SAQUES:
            print("Limite máximo diário de 3 saques ultrapassado!")

        elif saldo > valor:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque de: ---> {valor:.2f}\n"

        else:
            print("Falha na operação!")

    elif opcao == "e":
        print("\n=============Extrato=============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "f":
        print("Fechando...")
        break

    else:
        print("Opção inválida")