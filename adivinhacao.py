from random import randint

def adivinha(chute, resposta, jafoi = []):
        if chute != resposta:
            if chute not in jafoi:
                print("o chute foi maior doquê o numero secreto!" if chute > resposta else "o chute foi menor doquê o numero secreto!")
                jafoi.append(chute)
                return True
            else:
                print("esse número já foi chutado!")
                return True
        else:
            print("ACERTOU!!!")
            return False



numero = randint(1,10)

print("Bem vindo ao jogo de adivinhação")
loop = True
while loop:
    print(11*'===')
    palpite = input("Digite um número entre 1 e 10:")
    
    if palpite in ['1','2','3','4','5','6','7','8','9','10']:
        loop = adivinha(int(palpite),numero)
    else:
        print("entrada inválida digite um inteiro entre 1 e 10")
    