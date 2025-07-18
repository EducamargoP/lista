"""
O que o desafio pede?
Dada uma lista com 5 inteiros positivos, você deve:

Somar 4 de cada vez (excluindo 1 número diferente a cada vez).

Encontrar a menor soma possível e a maior soma possível.

Imprimir os dois valores em uma única linha, separados por espaço.
"""

def maior_menor(arr):
    total = sum(arr)
    minimo = total - max(arr)
    maximo = total - min(arr)
    print(minimo, maximo)

arr = list(map(int, input().split()))
maior_menor(arr)

