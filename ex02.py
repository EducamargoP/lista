## Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.

num = list()

while True:

    n = int(input("Digite um numero :"))
    if n not in num:
        num.append(n)
    else:
        print("numero ja existente! tente novamente")

    p = str(input("Deseja continuar [S/N] : ")) .strip().upper()
    if p in "Nn":
        break

print(sorted(num))