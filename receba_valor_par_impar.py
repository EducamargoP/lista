""" FAÇA UM PROGRAMA QUE LEIA 10 VALORES, ARMAZENE-OS EM UMA LISTA E  APRESENTE QUANTOS VALORES PARES ELE POSSUI"



"""

print("TODOS VALORES DEVERAM SER INTERIROS!")

valor1 = int(input('diga o primeiro valor:'))
valor2 = int(input('diga o segundo valor:'))
valor3 = int(input('diga o terceiro valor:'))
valor4 = int(input('diga o quarto valor:'))
valor5 = int(input('diga o quinto valor:'))
valor6 = int(input('diga o sexto valor:'))
valor7 = int(input('diga o setimo valor:'))
valor8 = int(input('diga o oitavo valor:'))
valor9 = int(input('diga o nono valor:'))
valor10 = int(input('diga o decimo valor:'))


lista = [valor1, valor2, valor3, valor4, valor5, valor6, valor7, valor8, valor9, valor10]


pares = []
impar = []

for num in lista:
    if  num % 2 == 0:
        pares.append(num)

    else:
        impar.append(num)
print(f'os numero pares foram {pares}')
print(f'os numero impares foram  {impar}')
print("FIM!")

