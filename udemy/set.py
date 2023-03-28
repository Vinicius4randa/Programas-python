listas = [
    [1,2,3,4,5,6,6,5,4,3,2,1],
    [1,2,3,2,3,1],
    [1,1,2,3,2,3],
    [1,2,3,4,5,6]
]

for atual in listas:
    count = 0
    repetido = None
    conjunto = set()

    while count != len(atual)-2:
        if atual[count] in conjunto:
            repetido = atual[count]
            break
        conjunto.add(atual[count])
        count+=1

    if repetido:
        print(repetido) 
    else:
        print(-1)  