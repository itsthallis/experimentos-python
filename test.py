
def dicionarios():
    produto = {
        "nome": "iPhone 6",
        "preco": 1299
    }
    for atributo in produto:
        print(atributo+': '+str(produto[atributo]))
    print(produto)


dicionarios()
