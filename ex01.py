## Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor

lista = []
mai = 0
men = 0
for c in range(0,5):
    lista.append(int(input(f"diga o valor da possição {c} : ")))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]

print('=-'*45)
if c in range(5):
  print(sorted(lista))
  print(f'menor numero digitado foi {men}')
  print(f'maior numero digitado foi {mai}')
