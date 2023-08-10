##Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

contador = []
par = []
impar = []


while True:
    num = int(input('diga o numero :'))
    contador.append(num)
    deseja = str(input('Deseja continuar ? [S/N]: ')).strip().upper()
    if deseja in 'Nn':
       break
for i, v in enumerate(contador):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print("=-"*40)
print(f'A lista completa é {contador}')
print(f'numero impares são {impar}')
print(f'numero pares são {par}')
