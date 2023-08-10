##Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

modelo = [[0,0,0],[0,0,0],[0,0,0]]

for l in range (0,3):
    for c in range (0,3):
        modelo[l][c] = int(input(f'Diga valor da casa[{c},{l}] :'))
print('-='*45)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{modelo[l][c]:^5}]', end='')
    print()