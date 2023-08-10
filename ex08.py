##Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]
for c in range(0,8):
   num = int(input("VALOR :"))
   if num % 2 == 0:
       lista[0].append(num)
   else:
       lista[1].append(num)
print("-="*40)
print(f"Dados completos : {lista}")
print(f"Os valores pares saõ  {lista[0]}")
print(f"Os valores impares são : {lista[1]}")