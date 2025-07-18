"""
Crie um programa que leia 5 nomes digitados pelo usuário e armazene em uma lista. Em seguida, exiba os nomes em ordem alfabética usando um loop."""


nomes = []

while len(nomes) < 5:
    nome = str(input('Diga seu nome: '))
    nomes.append(nome)

alf = sorted(nomes)
for nome in alf:
    print(nome)
