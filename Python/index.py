# Definindo as funções

def depositar(valor, extrato):
    global saldo
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de {valor:.2f} realizado com sucesso! \n")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return extrato

def sacar(valor, extrato, numero_saques, limite_saques, limite):
    global saldo 
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de {valor:.2f} realizado com sucesso! \n")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return extrato, numero_saques

def visualizar_extrato(extrato):
    global saldo  
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# menu principal

menu = """
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """


saldo = 0
extrato = ""
numero_saques = 0
limite = 500
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))
        extrato = depositar(valor, extrato)

    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))
        extrato, numero_saques = sacar(valor, extrato, numero_saques, LIMITE_SAQUES, limite)

    elif opcao == "2":
        visualizar_extrato(extrato)

    elif opcao == "3":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
