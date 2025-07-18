""""
Exercício 4: Conjunto com números únicos
Objetivo:

Crie um conjunto vazio

Use um loop while para pedir números ao usuário

Adicione os números ao conjunto

Continue até que o conjunto tenha 5 números únicos

Exiba o conjunto final
"""

numero = set()

while len(numero) < 5:
    num = int(input('diga um numero: '))
    numero.add(num)

print("Conjunto final:", numero)

