"""
 - CRIE UM PROGRAMA QUE LÊ 6 VALORES INTEIROS, ARMAZENE EM UMA LISTA E EM SEGUINDA MOSTRE NA TELA OS VALORES LIDOS

"""

print("TODOS OS VALORES DEVERAM SER INTEIROS!")
num1 = int(input('diga primeiro valor: '))
num2 = int(input('diga segundo valor: '))
num3 = int(input('diga terceiro valor: '))
num4 = int(input('diga quarto valor: '))
num5 = int(input('diga quinto valor: '))
num6 = int(input('diga ultimo valor: '))

lista = [num1, num2, num3, num4, num5, num6]
print(lista)
print("FIM DO PROGRAMA!")

"""
MANEIRA QUE FOI FEITA PELO PROFESSOR:
lista: list[int] = []
while len(lista) < 6:
    valor: int = int(input(f'informe o valor {len(lista) +1}/6: '))
    lista.append(Valor)
for valor in lista:
print(Valor)
"""