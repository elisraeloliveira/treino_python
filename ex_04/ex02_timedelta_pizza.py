from datetime import datetime, timedelta


pizza_small = 40
pizza_media = 60
pizza_large = 75
present_date = datetime.now()

while True:
    pizza = input("Sua pizza é de qual tamanho?\n ")  # P, M, G

    if pizza == "P":
        estimate_date = present_date + timedelta(minutes=pizza_small)
        print(f"Ótima escolha!\nSeu pedido foi feita ás {present_date.strftime('%H:%M:%S')}\nEle estará pronto às {estimate_date.strftime('%H:%M:%S')}")
        break

    elif pizza == "M":
        estimate_date = present_date + timedelta(minutes=pizza_media)
        print(f"Ótima escolha!\nSeu pedido foi feita ás {present_date.strftime('%H:%M:%S')}\nEle estará pronto ás {estimate_date.strftime('%H:%M:%S')}")
        break

    elif pizza == "G":
        estimate_date = present_date + timedelta(minutes=pizza_large)
        print(f"Ótima escolha!\nSeu pedido foi feita ás {present_date.strftime('%H:%M:%S')}\nEle estará pronto às {estimate_date.strftime('%H:%M:%S')}")
        break
    else:
        print(f"Pedido inválido! Repita o seu pedido\n{pizza}\n")



