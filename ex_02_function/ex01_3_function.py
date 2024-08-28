# colocando o input no argumento da função

def exibir_mensagem(nome = input("Digite seu nome: ")):
    print(f"Olá, {nome}!")

exibir_mensagem()