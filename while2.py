while True:
    nota = float(input('insira uma nota: '))
    if 0 <= nota <=10:
        print("a nota informada é válida :)")
        break
    print("a nota informada é inválida, tente novamente")