#exemplo 01

pessoa = {"nome": "Elisrael", "idade":30}
print(pessoa)

#exemplo 02

pessoa_ex02 = dict(nome = "Ana", idade = 29)
print(pessoa_ex02)

#exemplo de como adicionar item no dicionário

pessoa["telefone"] = "3333-3333"
print(pessoa)

print(pessoa_ex02["idade"]) #para acessar valores dentro de um dicionário

pessoa["nome"] = "Oliveira"  #método para modificação de dados
print(pessoa)