def criaMultiplicador(multiplicador):
    def multiplicar(numero):
        resultado = numero * multiplicador
        return resultado
    return multiplicar

num = int(input('insira o numero que será feita a tabuada:'))
for i in range (1,11):
    multiplica = criaMultiplicador(i)
    print(f'{num} * {i} = {multiplica(num)}')