# para incluir um item na lista, basta usar o [].append

lista = []

lista.append(1)
lista.append(5444.0)
lista.append("Olá")
lista.append([25, 2, 35])

print(lista)

#copiar a lista, usamos o [].copy()
lista2 = lista.copy()

print(f"cópia: {lista2}")

# para çlimpar uma lista usamos [].clear()
lista.clear()

print(lista)

#também podemos contar quantas vezes um elemento se repete na lista usando o [].count()
print(lista2.count("Olá"))

# querendo unir listas usamos 0 [].extend

some_languages = ["python", "java", "javascript"]
other_languages = ["csharp", "c++", "dolphin"]

print(some_languages)
print(other_languages)

some_languages.extend(other_languages)
print(some_languages)

# para saber onde certo elemento de uma lista se encontra, usamos o [].index()

print(some_languages.index("python"))
print(some_languages.index("csharp")) # nesta lista aqui, com a ordem do código, ela já uniu com outra lista(other_languages).

# se queremos remover um elemento, podemos usar o [].pop(), neste caso, sem nenhuma idicação de elemento, vai ser retirado o ultimo, como uma lista de pratos
print(some_languages.pop()) #retirou o ultimo
print(some_languages.pop(0)) # retirou o primeiro
print(some_languages) #print da lista atualizada

#já se quero remover um elemento expecifico, eu utilizo [].remove(), neste caso, fuciona declarando a classe fora do print

some_languages.remove("c++")
print(some_languages)