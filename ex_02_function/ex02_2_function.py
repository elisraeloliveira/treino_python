#argumentos nomeados

def salvar_carro(marca, modelo, ano, placa):
    print(f"\nCarro inserido com sucesso! \n {marca}/{modelo}/{ano}/{placa}")

#há 3 maneiras de argumentos nomeados:
salvar_carro("Fiat","Palio",1999,"ABC-1993")
#no modelo acima, o código sendo mudado de ordem no argumento da função, pode haver a confusão quando inserir os dados.

salvar_carro(marca="Ford",modelo="KA",ano=2019,placa="DEF-3991")
#no modelo acima, há uma segurança maior quanto a mudança de código no argumento da função.

salvar_carro(**{"marca":"Chevrolet","modelo":"Onix","ano":2018,"placa":"GHI-9319"})
#no modelo acima, crio um dicionário.


