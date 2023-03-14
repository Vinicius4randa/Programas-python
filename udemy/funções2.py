def criaMultiplicador(multiplicador):
    def multiplicar(numero):
        resultado = numero * multiplicador
        return resultado
    return multiplicar

num = int(input('insira o numero que será feita a tabuada:'))
for i in range (1,11):
    a = criaMultiplicador(i)
    print(a(num))