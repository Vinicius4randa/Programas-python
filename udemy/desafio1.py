def captal_indexes(palavra):
    lista = list(palavra)
    listaDeMaiusculos = []
    for n,i in enumerate(lista):
        if i == i.upper():
            listaDeMaiusculos.append(n)
    return listaDeMaiusculos
          

teste = captal_indexes("HeLlO")
print(teste)
