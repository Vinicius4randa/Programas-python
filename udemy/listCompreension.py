produtos = [
    {'nome' : 'banana', 'preço' : 10.00},
    {'nome' : 'café', 'preço' : 15.00},
    {'nome' : 'leite', 'preço' : 20.00}
    ]

novosProdutos = [
    {**produto, 'preço': produto['preço'] + 5} if produto['preço'] >= 20 else {**produto}
    for produto in produtos
]
for i in (novosProdutos):
    print(i)