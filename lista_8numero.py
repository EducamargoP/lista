"""Crie um programa que leia 8 números inteiros do usuário e armazene em uma tupla. Em seguida, exiba:

O maior valor da tupla

O menor valor da tupla

A quantidade de vezes que o número 3 aparece"""
from itertools import count

valores = []

while len(valores) < 8:
    num = int(input(f'diga o numero: '))
    valores.append(num)

tupla = tuple(valores)

print(f'o maior numero: {max(valores)}')
print(f'o menor numero: {min(valores)}')
print(f'o numero 3 aparece: {tupla.count(3)}')

