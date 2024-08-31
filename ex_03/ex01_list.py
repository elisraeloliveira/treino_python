numeros = [3, 30, 15, 24, 33, 28, 75, 72]
par = []
impar = []

for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(par, impar)