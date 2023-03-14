def multiplicaTodos(*numeros):
    acumulador = 1
    for i in numeros:
        acumulador *= i
    return acumulador



print(multiplicaTodos(1,2,3,4,5))