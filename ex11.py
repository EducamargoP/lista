##Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um

lista = []

while True:
    nome = str(input('NOME:'))
    nota1 = float(input('NOTA1:'))
    nota2 = float(input('NOTA2:'))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1,nota2], media])

    ## pergunta
    deseja = str(input('DESEJA CONTINUAR ? [S/N]:'))
    if deseja in 'Nn':
        break
print("=-="*28)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print("=-="*28)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

