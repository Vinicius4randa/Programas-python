from math import ceil

area = float(input("insira a area que deverá ser pintada: "))
tintaNecessaria = ceil((area * 1.1)/6)
situacao1 = ceil(tintaNecessaria/18)
gasto1 = (situacao1*18)-tintaNecessaria
situacao2 = ceil(tintaNecessaria/3.6)
gasto2 = (situacao2*3.6)-tintaNecessaria
situacao3 = [tintaNecessaria//18]
resto3 = tintaNecessaria % 18
situacao3.append(ceil(resto3/3.6))
gasto3 = (situacao3[0]*18) + (situacao3[1]*3.6)-tintaNecessaria

print(f"Para pintar {area} m², são necessários {tintaNecessaria}L de tinta.\nPara esta compra temos estas 3 opçãoes:")
print("=="*45)
print(f"+ situação 1 = {situacao1} latas de tinta(18L), R${situacao1*80:.2f} a pagar. Gasto de {gasto1:.1f}L.")
print(f"+ situação 2 = {situacao2} galões de tinta(3.6L), R${situacao2*25:.2f} a pagar. Gasto de {gasto2:.1f}L.")
print(f"+ situação 3 = {situacao3[0]} latas de tinta(18L), {situacao3[1]} galões de tinta(3.6L), R${situacao3[0]*80 + situacao3[1]*25:.2f} a pagar. Gasto de {gasto3:.1f}L.")
print("=="*45)
