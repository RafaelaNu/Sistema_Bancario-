import textwrap

def menu ():
    menu = ''' /n
    
    DIGITE A OPERACAO QUE DESEJA REALIZAR : 

    [1] DEPOSITAR 

    [2] SACAR 

    [3] VER EXTRATO

    [4] NOVA CONTA

    [5] LISTAR CONTAS

    [6] NOVO USUÁRIO

    [7] SAIR 

    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo_da_conta , valor, extrato,/):
    if valor > 0 :
        saldo_da_conta =+ valor
        extrato += f" Deposito:\tR$ {valor:.2f}\n"
        print("\n --- Deposito realizado com sucesso!---")
    else:
        print("\n--- Operação falhou! valor informado inválido!---")
    return saldo_da_conta , extrato


def sacar (*, saldo_da_conta , valor, extrato, limite, numero_de_saques_realizados, limite_de_saques):
        excedeu_saldo = valor > saldo_da_conta
        excedeu_valor_de_saque = valor > limite 
        excedeu_numero_de_saques = numero_de_saques_realizados >= limite_de_saques

        if excedeu_saldo :

            print(' Saldo Insuficiente!')

        elif excedeu_valor_de_saque:

            print(' Seu limite de saque diário e somente 500,00! ')

        elif excedeu_numero_de_saques :

            print(' Somente 3 saques diários sao permitidos ! ')   

        elif valor > 0 :
            saldo_da_conta -= valor
            extrato += f" Saque de: R$ {valor:.2f}\n "
            numero_de_saques_realizados += 1
            print(' Saque realizado com sucesso! ')

        else:
            print(' O valor informado é inválido!') 

        return saldo_da_conta , extrato 

def exibir_extrato (saldo_da_conta,/,*,extrato):
        print("\n _______________EXTRATO_______________")
        print(" Não foram Realizadas Movimentações!." if not extrato else extrato)
        print(f" Saldo: R$ {saldo_da_conta:.2f} \n")
        print(" ________________________________________")

def criar_usuario(usuarios):
    cpf = input("Informe o número de CPF: ")
    usuario = filtrar_usuario(cpf , usuarios)

    if usuario:
        print("\n--- já existe usuário com esse cpf! ---")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logradouro, número-bairro-cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,"cpf": cpf, "endereço": endereco})

    print("--- Usuário Criado com Sucesso!---")


def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia , numero_da_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n --- Conta Criada com Sucesso! ---")
        return{"agencia":agencia,"numero_da_conta": numero_da_conta, "usuario": usuario}
    
    print("\n--- Usuário nao encontrado , fluxo de criação de conta encerrado! ---")    


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_da_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo_da_conta = 0 
    limite = 500
    extrato = ""
    numero_de_saques_realizados = 0
    usuarios = []
    contas = []
 
    while True :
        opcao_do_usuario = menu()

        if opcao_do_usuario == "1":
            valor = float(input(" Informe o valor de Deposito: "))

            saldo_da_conta , extrato = depositar(saldo_da_conta, valor, extrato)

        elif opcao_do_usuario == "2":
            valor = float(input("Informe o valor do Saque: "))

            saldo_da_conta, extrato = sacar(
                saldo_da_conta = saldo_da_conta,
                valor = valor,
                extrato = extrato ,
                limite = limite,
                numero_de_saques_realizados = numero_de_saques_realizados,
                limite_de_saques = LIMITE_SAQUES,
            )    
        
        elif opcao_do_usuario == "3":
            exibir_extrato(saldo_da_conta, extrato = extrato)

        elif opcao_do_usuario == "4":
            numero_conta = len(contas) + 1 
            conta = criar_conta(AGENCIA, numero_conta,usuarios) 

            if conta:
                contas.append(conta) 

        elif opcao_do_usuario == "5":
            listar_contas(contas)

        elif opcao_do_usuario == "6" :
            criar_usuario (usuarios)

        elif opcao_do_usuario == "7":
            break

        else:
            print("Selecione novamente a operação desejada!") 

main()                            












