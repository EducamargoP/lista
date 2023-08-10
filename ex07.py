##Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram armazenadas. B) Uma listagem com  mais pesadas. c) Uma listagem com  mais leves.


lista = []
prin = []
total = 0
maior = menor = 0

while True:
    lista.append(str(input("NOME: ")))
    lista.append(float(input('PESO: ')))
    if len(prin) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    prin.append(lista[:])
    lista.clear()
    total += 1
    deseja = str(input('Deseja continuar ? [S/N]')).strip().upper()
    if deseja in 'Nn':
        break
print("=-"*40)
print(f"ao todo voce cadastrou  {total} pessoas")
print(f"os dados são {prin}")
print(f"Maior cadastrado foi {maior}")
print(f"Menor cadastrado foi {menor}")
print("=-"*40)

