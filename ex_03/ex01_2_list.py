numeros = [3, 30, 15, 24, 33, 28, 75, 72]
par = [numero for numero in numeros if numero %2 == 0]
impar = [numero for numero in numeros if  numero% 2 >= 1]

print(par, impar)

# metodo diferente de inclusão de itens numa nova lista