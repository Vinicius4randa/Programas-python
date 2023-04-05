limite = int(input('insira o numero de colunas de sua matriz: '))
xlinha = [
    (x,y)
    for x in range(limite)
    for y in range(limite)]

'''novamatriz = [
    [y,x] for y in xlinha for x in xlinha
]'''

for i in xlinha:
    print(i,end=' ')
    if i[1] == limite-1:
        print()