# Lista 2025 📘

Este repositório reúne meus estudos e resoluções de desafios em Python ao longo de 2025. Os exercícios são baseados em listas de prática, desafios de plataformas como HackerRank, e projetos pessoais.

## 📌 Estrutura

### 🧮 Desafios de lógica e listas

- `01-maior-menor.py`: Lê 5 valores e mostra o maior e o menor.
- `02-lista-valores.py`: Permite digitar vários valores e armazenar em uma lista.
- `03-insercao-ordenada.py`: Insere 5 valores já em ordem.
- `04-quantidade-ordenacao-verificacao.py`: Conta valores, ordena e verifica se o número 5 foi digitado.
- `05-pares-impares.py`: Separa valores pares e ímpares em listas diferentes.
- `06-validacao-parenteses.py`: Verifica se os parênteses estão corretamente fechados.
- `07-peso-pessoas.py`: Armazena nome e peso, mostra os mais leves e mais pesados.
- `08-pares-impares-ordenados.py`: Separa e ordena pares e ímpares.
- `09-matriz-3x3.py`: Cria e exibe uma matriz 3x3.
- `10-mega-sena.py`: Gera palpites aleatórios para a Mega Sena.
- `11-boletim-alunos.py`: Calcula média de alunos e exibe boletim.
- `12-mercado.py`: Simula um sistema de mercado com análise, atualização e exclusão de itens.

### 🌐 Desafios HackerRank

- `plusMinus.py`: Calcula proporções de positivos, negativos e zeros.
- `miniMaxSum.py`: Soma mínima e máxima de 4 entre 5 inteiros.

## 🚀 Objetivo

Praticar lógica de programação, algoritmos e estrutura de dados com foco em desenvolvimento backend e análise de dados.

## 🛠️ Tecnologias

- Python 3.x
- Git & GitHub
- VS Code

## ✍️ Autor

**Eduardo Camargo Paulino**  
Cursando Análise e Desenvolvimento de Sistemas  
Apaixonado por tecnologia, segurança da informação e desenvolvimento web.

Aula: Trabalhando com Listas em Python
📌 1. O que são listas?
Listas em Python funcionam como vetores ou matrizes em outras linguagens, mas com um diferencial: são dinâmicas e podem armazenar qualquer tipo de dado.

Diferente de linguagens como C e Java, em que os arrays precisam ser declarados com um tipo fixo (inteiro, string etc), em Python a lista pode mudar e ser manipulada livremente.

📌 2. Como declarar uma lista?
Listas em Python são representadas por colchetes []:

python
minha_lista = [1, 2, 3, "texto", True]
🔍 Operações comuns com listas
✅ 3. Verificar se um valor está na lista:
python
lista = list(range(11))  # gera valores de 0 a 10
if 8 in lista:
    print("Encontrei o número 8")
else:
    print("Não encontrei o número 8")
✅ 4. Ordenar uma lista:
python
lista.sort()
print(lista)
✅ 5. Contar ocorrências de um valor:
python
print(lista.count(3))  # Conta quantas vezes o número 3 aparece
➕ Adicionando elementos
✅ 6. Adicionar com append() (1 elemento por vez):
python
lista.append(42)
✅ 7. Adicionar com extend() (vários elementos):
python
lista.extend([10, 20, 30])
⚠️ extend() aceita apenas coleções como listas — não valores únicos.

✅ 8. Inserir elemento em posição específica:
python
lista.insert(2, "novo valor")
➡ Isso não substitui o valor no índice, apenas o realoca.

🔄 Outras manipulações
✅ 9. Juntar duas listas:
python
lista_final = lista1 + lista2
✅ 10. Reverter a ordem da lista:
python
lista.reverse()
✅ 11. Copiar uma lista:
python
lista_copia = lista.copy()
✅ 12. Obter o tamanho da lista:
python
print(len(lista))
✅ 13. Remover último elemento com pop():
python
lista.pop()  # remove o último e retorna o valor removido
✅ 14. Apagar todos os elementos da lista:
python
lista.clear()
🧪 Funções extras
✅ 15. Repetir elementos da lista:
python
nova_lista = ["A"] * 3  # ['A', 'A', 'A']
✅ 16. Converter string em lista:
python
texto = "Eduardo Camargo"
lista_de_palavras = texto.split()
✅ 17. Converter lista em string:
python
texto_unido = ' '.join(lista_de_palavras)
➡ Pode substituir o espaço por qualquer separador: '$', '|' etc.

📚 Acesso e busca
✅ 18. Acessar elementos por índice:
python
print(lista[2])
✅ 19. Descobrir posição de um valor com index():
python
print(lista.index(10))  # retorna o primeiro índice encontrado
✂️ Fatiamento (slicing)
✅ 20. Sintaxe:
python
lista[inicio:fim:passo]
range(inicio, fim, passo)
Exemplo:

python
print(lista[1:6:2])  # do índice 1 ao 5, pulando de 2 em 2
➕ Funções matemáticas (com números inteiros)
python
lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # Soma total
print(max(lista))  # Maior valor
print(min(lista))  # Menor valor
print(len(lista))  # Quantidade de elementos
🔄 Tuplas x Listas
Tuplas usam parênteses ( ) e são imutáveis.

Listas usam colchetes [ ] e são mutáveis.

📎 Copiando listas
✅ Deep copy (cópia verdadeira):
python
lista = [1, 2, 3, 4]
nova_lista = lista.copy()
nova_lista.append(5)
print(lista)       # [1, 2, 3, 4]
print(nova_lista)  # [1, 2, 3, 4, 5]
✅ Shallow copy (referência compartilhada):
python
lista = [1, 2, 3, 4]
nova_lista = lista
nova_lista.append(5)
print(lista)       # [1, 2, 3, 4, 5]
print(nova_lista)  # [1, 2, 3, 4, 5]
