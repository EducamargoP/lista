## Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção
cont = []

for c in range(0,5):

    con = int(input("Digite um numero [0/10]:"))
    if cont == 0 :
        cont.append(con)
    else:
        pos = 0
        while pos < len(cont):
            if con <= cont[pos]:
                cont.append(pos, con)
                break
            pos += 1


print("=-"*40)
print(f"os numero foram : {con}")
print("=-"*40)
