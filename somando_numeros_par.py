"""
Exercício 1: Soma de números pares
Objetivo:

Crie uma lista com os números de 1 a 20

Use um loop for para percorrer a lista

Identifique os números pares

Some os pares

Exiba o resultado da soma
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

par = []
impar = []

for num in lista:
    if num % 2 == 0:
        par.append(num)
print(par)
print(sum(par))