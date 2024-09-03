#dicionários aninhados

contatos = {
    "elisrael@oliveira.com": {"nome": "Elisrael", "telefone" : "3333-3333"},
    "anacarolina@oliveira": {"nome":"Ana Carolina","telefone":"4444-4444"},
    "frederico@oliveira.com":{"nome": "Frederico", "telefone": "5555-5555"},
}

print(contatos["elisrael@oliveira.com"]["nome"])

#posso tambem incluir a minha seleção do dicionário numa variável, neste ponto é bom para quando no dicionário há apenas um item numa lista


telefone = contatos["elisrael@oliveira.com"]["telefone"]
print(telefone)
