# Lista que armazenará todas as transações
transacoes = []

saldo = 0

while True:
    print("\n=== CONTROLE FINANCEIRO JOVEM ===")
    print("1 - Adicionar entrada")
    print("2 - Adicionar gasto")
    print("3 - Ver saldo")
    print("4 - Ver transações")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Valor da entrada: "))
        categoria = input("Categoria: ")

        saldo += valor

        transacoes.append({
            "tipo": "Entrada",
            "valor": valor,
            "categoria": categoria
        })

        print("Entrada registrada com sucesso!")

    elif opcao == "2":
        valor = float(input("Valor do gasto: "))
        categoria = input("Categoria: ")

        if valor <= saldo:
            saldo -= valor

            transacoes.append({
                "tipo": "Gasto",
                "valor": valor,
                "categoria": categoria
            })

            print("Gasto registrado com sucesso!")
        else:
            print("Saldo insuficiente!")

    elif opcao == "3":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        print("\n=== HISTÓRICO DE TRANSAÇÕES ===")

        if len(transacoes) == 0:
            print("Nenhuma transação cadastrada.")
        else:
            for i, t in enumerate(transacoes, start=1):
                print(
                    f"{i}. {t['tipo']} | "
                    f"R$ {t['valor']:.2f} | "
                    f"{t['categoria']}"
                )

    elif opcao == "5":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")