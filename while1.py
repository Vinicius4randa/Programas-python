impares = 0
while impares < 10:
    novoNumero = float(input('digite um número: '))
    impares += 1 if novoNumero%2 != 0 else 0
print("já coletei 10 números impares")