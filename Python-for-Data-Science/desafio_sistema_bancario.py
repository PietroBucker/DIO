MENU = """
[A]-EXTRATO
[B]-SAQUE
[C]-DEPOSITO
[D]-SAIR
"""

saques_dia = 3
limite_saque = 500
movimenta = False
qtd_saque = 0
extrato = {
    "saldo": 0,
    "depositos": [],
    "saques": [],
}

while True:
    options = input(MENU).upper()

    if options == "C":
        value = int(input("Digite o valor a ser depositado:"))
        if value > 0:
            extrato["saldo"] += value
            extrato["depositos"].append(value)
            movimenta = True
            continue
        else:
            print("Digite apenas valores positivos")
            continue

    if options == "B":
        value = int(input("Digite o valor a ser sacado: "))

        if qtd_saque < saques_dia and 0 < value <= limite_saque:
            if value <= extrato["saldo"]:
                print("valor esta sendo processado")
                extrato["saldo"] -= value
                extrato["saques"].append(value)
                qtd_saque += 1
                movimenta = True
                continue

            else:
                print("saldo insuficiente")
                continue

        else:
            print("nao foi possivel concluir a operaçao")
            continue

    if options == "A":
        print(
            f"""
            #####EXTRATO#####
            {
            'Nao foram realizadas movimentações'
            if not movimenta else 'Movimentação'
            }
            Saldo: R${extrato['saldo']:.2f}
            Saques: {[f'R${s:.2f}' for s in extrato['saques']]}
            Depositos: {[f'R${d:.2f}' for d in extrato['depositos']]}
            """
        )
        continue

    if options == "D":
        break

    else:
        print(f"Opção: {options} invalido, tente novamente")
