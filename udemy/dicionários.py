questoes = [{
    'questão': 'quanto é 2+2',
    'alternativas': [1,2,3,4,5],
    'resposta' : 4
},
{
    'questão': 'quanto é 5+2',
    'alternativas': [9,7,13,3,5],
    'resposta' : 7
},
{
    'questão': 'quanto é 2+1',
    'alternativas': [1,2,3,4,5],
    'resposta' : 3
}]

for q in questoes:
    print('='*25)
    print(f"{q['questão']}?\n")
    count = 1
    for a in q['alternativas']:
        print(f'{count}) {a}')
        count+=1
    resposta = int(input("\nresposta: "))
    print('CORRETO' if resposta == q['resposta'] else 'ERRADO')
    