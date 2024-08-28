# retornando valores


def calcular_total(numeros):
    return sum(numeros)

def retorne_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor,sucessor

print(calcular_total([10, 30, 50]))
print(retorne_antecessor_e_sucessor(10))


