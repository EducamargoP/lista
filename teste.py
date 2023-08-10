##Programa de mercado (analise, compra, entrada e saida)
print("=-"*40)
print("Bem-vindo ao Mercado")
lista = []
while True:
    escolha = str(input("""[1] ADICIONAR PRODUTO [2] ATUALIZAR PRODUTO [3] ESTOQUE
    escolha uma opção : """))
    print("=-"*40)
    ##Adicionar
    if escolha == "1":
        adiciona = str(input("PRODUTO : "))
        quantidade = int(input('QUANTIDADE: '))
        valor = float(input("VALOR UNIDADE R$:"))
        lista.append(adiciona)
        lista.append(quantidade)
        lista.append(valor)
        soma = valor * quantidade
        print(f"produto {adiciona} com um valor de unidade R$: {valor} caixa no valor de R$: {soma}")
    ##Atualizar
    elif escolha == "2":
        atualiza = str(input('NOME :'))
        quantidade = int(input("QUANTIDADE :"))
        preco = float(input("VALOR :"))
        lista[0] = atualiza
        lista[1] = quantidade
        lista[2] = preco
        soma = quantidade * preco
        print(f"Produto atualizado : {atualiza} com o valor de unidade R$: {preco} valor da caixa {soma} ")
    ##estoque
    else:
        print('PRODUTO - QUANTIDADE - VALOR UNIDADE')
        print(lista)
        break



