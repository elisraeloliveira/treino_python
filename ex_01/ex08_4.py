# neste código, usei a condição ternária.
#In this code, I used the ternary condition

saldo = 1000.00
saque = float(input("Digite o valor para saque:  "))

status = "Sucesso" if saldo >= saque else "Falha"


print(f'{status} ao realizar o saque!')