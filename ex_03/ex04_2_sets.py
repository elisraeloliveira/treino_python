# os sets não suportam indexação e nem fatiamento
# para acessar os valores, é necessário converter o conjunto

numero = {1, 2, 3, 4}
#print(numero[1])    #neste exemplo dá erro, no código abaixo está o metodo correto.

numero = list(numero)

print(numero[1])

# porém a forma comum de percorrer os dados de um set é utilizando um for

carros = {"palio", "corsa", "gol"}

for carro in carros:
    print(carro)

