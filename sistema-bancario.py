from datetime import datetime

# Listas globais para armazenar usuários e contas
usuarios = []
contas = []

# Função para criar usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    """
    Cria um novo usuário e adiciona à lista de usuários.
    
    Args:
        nome (str): Nome do usuário.
        data_nascimento (str): Data de nascimento no formato dd/mm/yyyy.
        cpf (str): CPF do usuário (somente números).
        endereco (str): Endereço no formato 'logradouro, nro - bairro - cidade/sigla estado'.
    
    Returns:
        str: Mensagem de sucesso ou erro.
    """
    # Verifica se o CPF já está cadastrado
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        return "❌ Usuário já cadastrado com este CPF."
    
    # Cria o usuário
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    return "✅ Usuário criado com sucesso!"

# Função para criar conta corrente
def criar_conta_corrente(cpf):
    """
    Cria uma nova conta corrente vinculada a um usuário.
    
    Args:
        cpf (str): CPF do usuário que será vinculado à conta.
    
    Returns:
        str: Mensagem de sucesso ou erro.
    """
    # Filtra o usuário pelo CPF
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if not usuario:
        return "❌ Usuário não encontrado. Verifique o CPF informado."
    
    # Gera número da conta sequencial
    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    return f"✅ Conta criada com sucesso! Agência: 0001, Número da conta: {numero_conta}"

# Função de saque (keyword-only arguments)
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque na conta, respeitando o limite e o número máximo de saques.
    
    Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor do saque.
        extrato (list): Lista de transações.
        limite (float): Limite máximo para saque.
        numero_saques (int): Número de saques realizados hoje.
        limite_saques (int): Limite máximo de saques diários.
    
    Returns:
        tuple: Saldo atualizado e extrato atualizado.
    """
    if numero_saques >= limite_saques:
        print("❌ Limite de saques diários atingido.")
        return saldo, extrato
    if valor > limite:
        print("❌ Valor excede o limite permitido para saque.")
        return saldo, extrato
    if valor > saldo:
        print("❌ Saldo insuficiente.")
        return saldo, extrato
    if valor <= 0:
        print("❌ Valor inválido para saque.")
        return saldo, extrato

    saldo -= valor
    extrato.append({"tipo": "saque", "valor": valor, "data_hora": datetime.now()})
    print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

# Função de depósito (positional-only arguments)
def deposito(saldo, valor, extrato, /):
    """
    Realiza um depósito na conta.
    
    Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor do depósito.
        extrato (list): Lista de transações.
    
    Returns:
        tuple: Saldo atualizado e extrato atualizado.
    """
    if valor <= 0:
        print("❌ Valor inválido para depósito.")
        return saldo, extrato

    saldo += valor
    extrato.append({"tipo": "depósito", "valor": valor, "data_hora": datetime.now()})
    print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

# Função de extrato (positional and keyword arguments)
def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta, mostrando saldo e transações.
    
    Args:
        saldo (float): Saldo atual da conta.
        extrato (list): Lista de transações.
    
    Returns:
        None
    """
    print("\n=================== Extrato Bancário ====================")
    print("📌 Transações:")

    if extrato:
        for transacao in extrato:
            data_formatada = transacao["data_hora"].strftime("%d/%m/%Y %H:%M:%S")
            print(f"   - {transacao['tipo'].capitalize()}: R$ {transacao['valor']:.2f} em {data_formatada}")
    else:
        print("   Nenhuma transação registrada.")

    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")
    print("=======================================================")

# Função para listar contas
def listar_contas():
    """
    Lista todas as contas cadastradas no sistema.
    
    Returns:
        None
    """
    print("\n=================== Contas Cadastradas ====================")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")
    print("==========================================================")

# Função principal para executar o sistema
def main():
    """
    Menu interativo para executar o sistema bancário.
    """
    saldo = 0.0
    extrato = []
    limite = 500.0
    limite_saques = 3
    numero_saques = 0

    while True:
        print("\n--- Sistema Bancário Modularizado ---")
        print("1️⃣ Criar Usuário")
        print("2️⃣ Criar Conta Corrente")
        print("3️⃣ Depositar")
        print("4️⃣ Sacar")
        print("5️⃣ Exibir Extrato")
        print("6️⃣ Listar Contas")
        print("7️⃣ Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            data_nascimento = input("Data de nascimento (dd/mm/yyyy): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            print(criar_usuario(nome, data_nascimento, cpf, endereco))
        elif opcao == "2":
            cpf = input("CPF do usuário: ")
            print(criar_conta_corrente(cpf))
        elif opcao == "3":
            try:
                valor = float(input("Digite o valor para depositar: "))
                saldo, extrato = deposito(saldo, valor, extrato)
            except ValueError:
                print("❌ Entrada inválida. Por favor, insira um valor numérico.")
        elif opcao == "4":
            try:
                valor = float(input("Digite o valor para sacar: "))
                saldo, extrato = saque(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=limite_saques
                )
                if saldo != 0:  # Incrementa número de saques apenas se o saque for bem-sucedido
                    numero_saques += 1
            except ValueError:
                print("❌ Entrada inválida. Por favor, insira um valor numérico.")
        elif opcao == "5":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "6":
            listar_contas()
        elif opcao == "7":
            print("👋 Obrigado por usar o sistema bancário. Até logo!")
            break
        else:
            print("❌ Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()