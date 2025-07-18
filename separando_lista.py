"""
Crie um programa que leia 10 números e armazene em uma lista. O programa deve:

Separar os números pares em uma nova lista

Separar os números ímpares em outra lista

Mostrar as duas listas separadamente
"""

lista = []

par = []
impar = []
while len(lista) < 10:
    num = int(input(f'diga numero {len(lista)+1}:'))
    lista.append(num)
for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'OS NUMERO PARES FORAM: {par}')
print(f'OS NUMERO IMPAR FORAM: {impar}')

