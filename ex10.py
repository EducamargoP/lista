##Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
print("=-"*30)
print('    JOGA NA MEGA      ')
print("=-"*30)

lista = []
jogos = []


pergunta = int(input("QUANTOS JOGOS DESEJA : "))
tot = 1
while tot <= pergunta:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-'*3, f'SORTEANDO {pergunta}','=-'*3)
for i, l in enumerate(jogos):
    print(f' jogos {i}  {l}:')