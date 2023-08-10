##Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
##  A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

numero = []

while True:
    num = int(input("Diga valor :"))
    numero.append(num)
    desejo = str(input("Deseja continuar [S/N] :")).strip().upper()
    if desejo in 'Nn':
      break


numero.sort(reverse=True)
print(f"Os numero decrecente sao : {numero}")
print(f"Voce digitou {len(numero)} valores")
if 5 in numero:
    print("Numero 5 esta nos valores")
else:
    print("Numero 5 nao faz parte !")