"""
 Verificação de fruta
Objetivo:

Crie uma tupla com frutas: ("maçã", "banana", "laranja", "abacaxi", "uva")

Peça ao usuário para digitar o nome de uma fruta

Use um loop for para verificar se a fruta está na tupla

Se estiver, exiba "Fruta encontrada!"

Se não estiver, exiba "Fruta não encontrada."
"""
from operator import truediv

tupla = ("maçã", "banana", "laranja", "abacaxi", "uva")

usuario = str(input("DIGA UMA FRUTA: "))

encontrada = False

for fruta in tupla:
    if fruta == usuario:
        encontrada = True
        break
if encontrada:
    print('Fruta encontrada')
else:
    print("Essa fruta nao temos")

