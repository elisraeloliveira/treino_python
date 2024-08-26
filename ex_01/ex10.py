opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:   "))

    if opcao == 1:
        print("Sacando\n")
    elif opcao == 2:
        print("Exibindo extrato...\n")
    elif opcao == 0:
        print("Transação finalizada!")

    else: print("Opção invalida, tente novamente.\n")