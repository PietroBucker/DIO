MENU = """
[C]-Nova Conta
[E]-EXTRATO
[S]-SAQUE
[D]-DEPOSITO
[Q]-SAIR
"""

LOGIN = "[ ]-CPF para entrar na conta: "


banco = {"usuarios": dict()}


def deposito(extrato, /):
    value = int(input("Digite o valor a ser depositado: "))
    if value > 0:
        extrato["saldo"] += value
        extrato["depositos"].append(value)
        extrato["movimenta"] = True
        return
    else:
        print("Digite apenas valores positivos")
        return


def saque(*, extrato):
    value = int(input("Digite o valor a ser sacado: "))
    if (
        extrato["qtd_saque"] < extrato["saques_dia"]
        and 0 < value <= extrato["limite_saque"]
    ):
        if value <= extrato["saldo"]:
            print("valor esta sendo processado")
            extrato["saldo"] -= value
            extrato["saques"].append(value)
            extrato["qtd_saque"] += 1
            extrato["movimenta"] = True
            return
        else:
            print("saldo insuficiente")
            return
    else:
        print("nao foi possivel concluir a operaçao")
        return


def extrat(extrato):
    print(
        f"""
            #####EXTRATO#####
            {
            'Nao foram realizadas movimentações'
            if not extrato["movimenta"] else 'Movimentação'
            }
            Saldo: R${extrato['saldo']:.2f}
            Saques: {[f'R${s:.2f}' for s in extrato['saques']]}
            Depositos: {[f'R${d:.2f}' for d in extrato['depositos']]}
            """
    )


def novo_usuario(banco):
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    endereco = input("Digite seu endereço: ")

    banco["usuarios"][cpf] = {
        "nome": nome,
        "idade": idade,
        "endereco": endereco,
        "conta": [
            {
                "ag": "0001",
                "n_conta": 1,
                "extrato": {
                    "saldo": 0,
                    "depositos": list(),
                    "saques": list(),
                    "movimenta": False,
                    "qtd_saque": 0,
                    "limite_saque": 500,
                    "saques_dia": 3,
                },
            },
        ],
    }
    return


def nova_conta(banco):
    cpf = input("Digite seu CPF")
    qtd_contas = len(banco["usuarios"][cpf]["conta"])
    print(qtd_contas)
    banco["usuarios"][cpf]["conta"].append(
        {
            "ag": "0001",
            "n_conta": qtd_contas + 1,
            "extrato": {
                "saldo": 0,
                "depositos": list(),
                "saques": list(),
                "movimenta": False,
                "qtd_saque": 0,
                "limite_saque": 500,
                "saques_dia": 3,
            },
        }
    )
    return


while True:
    login = input(LOGIN).upper()

    if login not in banco["usuarios"]:
        print("### Crie sua conta ###")
        novo_usuario(banco)
        continue

    else:
        options = input(MENU).upper()

        if options == "C":
            nova_conta(banco)
            continue

        if options == "D":
            try:
                n_conta = int(input("Para qual conta é essa operação: "))
                deposito(
                    banco["usuarios"][login]["conta"][n_conta - 1]["extrato"]
                )
                continue
            except Exception:
                print("Algo deu errado tente novamente")
                continue

        if options == "S":
            try:
                n_conta = int(input("Para qual conta é essa operação: "))
                saque(
                    extrato=banco["usuarios"][login]["conta"][n_conta - 1][
                        "extrato"
                    ]
                )
                continue
            except Exception:
                print("Algo deu errado tente novamente")
                continue
        if options == "E":
            try:
                n_conta = int(input("Para qual conta é essa operação: "))
                extrat(
                    banco["usuarios"][login]["conta"][n_conta - 1]["extrato"]
                )
                continue
            except Exception:
                print("Algo deu errado tente novamente")
                continue

        if options == "Q":
            break

        else:
            print(f"Opção: {options} invalido, tente novamente")
