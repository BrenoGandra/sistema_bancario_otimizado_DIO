#informações iniciais
usuarios = []
contas = []
numero_conta_sequencial = 1

#função para criar um usuário no sistema bancário
def criar_usuario(usuarios):
    cpf = input("Informe os números do CPF: ")    
    if any(usuario['cpf'] == cpf for usuario in usuarios): # aqui se aplica um filtro nos usuarios
        print("Não foi possível continuar pois o CPF já está cadastrado.")
        return
    
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereço completo (logradouro, bairro, cidade): ")

    usuarios.append({"cpf": cpf, "nome": nome, "nascimento": data_nascimento, "endereco": endereco}) #aqui adiciona o usuario numa lista
    print("Usuário cadastrado com sucesso.")

#função de criar uma conta corrente
def criar_conta_corrente(agencia, numero_conta, usuarios, contas):
    cpf = input ("Digite os números do cpf: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario:
        contas.append({"usuario": usuario, "agencia": agencia, "numero_conta": numero_conta}) #aqui adiciona a conta a uma lista
        print("Conta criada com sucesso.")
        return numero_conta + 1
    
    else:
        print("Não foi possível achar o usuário. ")
        return numero_conta

#função para listar os usuários cadastrados
def listar_usuarios():
    if not usuarios:
        print("Não há usuários cadastrados.") #aqui filtra para ver se há usuários cadastrados 
        return
    
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Nascimento: {usuario['nascimento']}, Endereço: {usuario['endereco']}") #aqui mostra os usuários cadastrados

#função de saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques
    
    if excedeu_limite:
        print("Não foi possível continuar pois o limite foi excedido.")

    elif excedeu_saldo:
        print("Não foi possível continuar pois não há saldo suficiente.")

    elif excedeu_saque:
        print("Não foi possível continuar pois o limite de saques foi atingido.")

    elif valor > 0:
        saldo -= valor #retira o valor do saldo existente 
        extrato += f"Valor saque: R$: {valor:.2f}\n" #aqui adiciona o valor no extrato
        numero_saques += 1 #adiciona contagem de saques
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

    else:
        print("Erro! digite um valor válido.")    

    return saldo, extrato, numero_saques  

#função de depósito
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor #adiciona o valor no saldo
        extrato += f"Depósito de R$: {valor:.2f}\n" #adiciona o valor no extrato
        print(f"Depósito de R$: {valor:.2f} realizado com sucesso.")

    else:
        print("Você digitou um valor inválido.\nTente novamente.")    

    return saldo, extrato    

#função de mostrar o extrato
def mostrar_extrato(saldo, /, *, extrato ):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def main():
    saldo = 0
    limite = 500
    LIMITE_SAQUES = 3
    numero_saques = 0
    extrato = ''
    agencia = "0001"
    global numero_conta_sequencial  

    menu = """
    [u] Cadastrar Usuário
    [c] Criar Conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
         

        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta_sequencial = criar_conta_corrente(agencia,numero_conta_sequencial,usuarios, contas)
            

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente.")

# função principal do sistema
main()



