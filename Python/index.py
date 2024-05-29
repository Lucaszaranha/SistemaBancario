# Definindo as funções


usuarios = []  # Lista para armazenar os usuários
contas_correntes = []  # Lista para armazenar as contas correntes
numero_conta = 1  # Primeiro digito da conta

def vincular_usuario_por_cpf(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None  # Retorna None se nenhum usuário com o CPF fornecido for encontrado

def criar_usuario():
    nome = input("Informe o nome do cliente: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Informe o CPF do cliente: ")

    # Verificar se já existe algum usuário com o mesmo CPF
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro: Já existe um usuário cadastrado com este CPF.")
            return None
    
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade/estado): ")

    # Armazenar apenas os números do CPF
    cpf_numeros = ''.join(filter(str.isdigit, cpf))

    # Criar dicionário representando o usuário
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_numeros,
        "endereco": endereco
    }

    # Adicionar usuário à lista de usuários
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuario

def criar_conta_corrente(usuario):
    global numero_conta
    
    # Agência fixa
    agencia = "0001"
    
    # Número da conta sequencial
    numero = numero_conta
    numero_conta += 1

    # Buscar o usuário pelo CPF
    usuario = vincular_usuario_por_cpf(cpf)
    if usuario is None:
        print("Erro: Nenhum usuário encontrado com o CPF fornecido.")
        return None
    
    # Criar dicionário representando a conta corrente
    conta_corrente = {
        "agencia": agencia,
        "numero": numero,
        "usuario": usuario
    }

    # Adicionar conta corrente à lista de contas correntes
    contas_correntes.append(conta_corrente)
    print("Conta corrente criada com sucesso!")
    return conta_corrente


def depositar(valor, extrato):
    global saldo
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de {valor:.2f} realizado com sucesso! \n")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return extrato

def sacar(*,valor, extrato, numero_saques, limite_saques, limite):
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

def visualizar_extrato(extrato, saldo=None):
    if saldo is not None:

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    else:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("==========================================")

usuarios = []

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
        extrato, numero_saques = sacar(valor=valor, extrato=extrato, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES, limite=limite)


    elif opcao == "2":
        visualizar_extrato(extrato)
        visualizar_extrato(extrato, saldo=saldo)


    elif opcao == "3":
        print("Obrigado por utilizar nosso app!...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
