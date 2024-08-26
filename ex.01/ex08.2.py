# neste código, foi mudado as condições de apenas if's, para conter if/else.
# In this code, the conditions were changed from only if statements to include if/else statements

saldo = 2000.0
saque  = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")