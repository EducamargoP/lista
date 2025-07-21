# 📘 Lista 2025 – Desafios em Python

Este repositório reúne meus estudos e resoluções de desafios em Python ao longo de 2025. Os exercícios são baseados em listas de prática, desafios de plataformas como HackerRank, e projetos pessoais com foco em lógica, algoritmos e estruturas de dados.

---

## 📌 Estrutura do Repositório

### 🧮 Desafios de lógica e listas

| Arquivo                        | Descrição                                                                 |
|-------------------------------|---------------------------------------------------------------------------|
| `01-maior-menor.py`           | Lê 5 valores e mostra o maior e o menor.                                 |
| `02-lista-valores.py`         | Permite digitar vários valores e armazenar em uma lista.                 |
| `03-insercao-ordenada.py`     | Insere 5 valores já em ordem.                                            |
| `04-quantidade-ordenacao.py`  | Conta valores, ordena e verifica se o número 5 foi digitado.             |
| `05-pares-impares.py`         | Separa valores pares e ímpares em listas diferentes.                     |
| `06-validacao-parenteses.py`  | Verifica se os parênteses estão corretamente fechados.                   |
| `07-peso-pessoas.py`          | Armazena nome e peso, mostra os mais leves e os mais pesados.            |
| `08-pares-impares-ordenados.py` | Separa e ordena pares e ímpares.                                       |
| `09-matriz-3x3.py`            | Cria e exibe uma matriz 3x3.                                             |
| `10-mega-sena.py`             | Gera palpites aleatórios para a Mega Sena.                               |
| `11-boletim-alunos.py`        | Calcula média de alunos e exibe boletim.                                 |
| `12-mercado.py`               | Simula um sistema de mercado com análise, atualização e exclusão.        |

---

### 🌐 Desafios HackerRank

| Arquivo             | Descrição                                                                 |
|---------------------|---------------------------------------------------------------------------|
| `plusMinus.py`      | Calcula proporções de positivos, negativos e zeros.                       |
| `miniMaxSum.py`     | Soma mínima e máxima de 4 entre 5 inteiros.                               |

---

## 🚀 Objetivo

Praticar lógica de programação, algoritmos e estrutura de dados com foco em desenvolvimento **backend** e **análise de dados**.

---

## 🛠️ Tecnologias utilizadas

- Python 3.x  
- Git & GitHub  
- VS Code

---

## ✍️ Autor

**Eduardo Camargo Paulino**  
Estudante de Análise e Desenvolvimento de Sistemas  
Apaixonado por tecnologia, segurança da informação e desenvolvimento web.

---

## 📘 Aula: Trabalhando com Listas em Python

As listas em Python funcionam como vetores/matrizes em outras linguagens, mas com o diferencial de serem **dinâmicas** e **multitipo**.

### 🔢 Declaração de lista:
```python
minha_lista = [1, 2, 3, "texto", True]
```

---

### 🔍 Operações comuns

- **Verificar valor**:
  ```python
  if 8 in lista:
      print("Encontrei o número 8")
  ```
- **Ordenar**:
  ```python
  lista.sort()
  ```
- **Contar ocorrências**:
  ```python
  lista.count(3)
  ```
- **Adicionar elemento**:
  ```python
  lista.append(42)          # Um por vez
  lista.extend([10, 20])    # Vários de uma vez
  ```
- **Inserir por índice**:
  ```python
  lista.insert(2, "novo valor")
  ```

---

### 🔁 Manipulações

- **Juntar listas**:
  ```python
  lista_final = lista1 + lista2
  ```
- **Reverter ordem**:
  ```python
  lista.reverse()
  ```
- **Copiar lista**:
  ```python
  lista_copia = lista.copy()
  ```
- **Tamanho da lista**:
  ```python
  len(lista)
  ```
- **Remover elementos**:
  ```python
  lista.pop()      # Remove o último
  lista.clear()    # Remove todos
  ```

---

### 💡 Extras úteis

- **Repetir elementos**:
  ```python
  nova = ["A"] * 3
  ```
- **Converter string para lista**:
  ```python
  frase = "Eduardo Camargo"
  palavras = frase.split()
  ```
- **Converter lista para string**:
  ```python
  texto = ' '.join(palavras)
  ```

---

### 📚 Acesso e busca

- **Acessar por índice**:
  ```python
  lista[2]
  ```
- **Localizar posição**:
  ```python
  lista.index("valor")
  ```

---

### ✂️ Fatiamento (slicing)

```python
lista[início:fim:passo]
range(início, fim, passo)
```

Exemplo:
```python
print(lista[1:6:2])
```

---

### 📊 Funções matemáticas (com números inteiros)

```python
lista = [1, 2, 3, 4, 5]
sum(lista)      # Soma total
max(lista)      # Maior valor
min(lista)      # Menor valor
len(lista)      # Quantidade de elementos
```

---

### 🔒 Tupla vs Lista

- Tupla → `(1, 2, 3)` → **imutável**
- Lista → `[1, 2, 3]` → **mutável**

---

### 🧬 Copiando listas

- **Deep copy**:
  ```python
  nova = lista.copy()
  nova.append(5)
  print(lista)       # [1, 2, 3]
  print(nova)        # [1, 2, 3, 5]
  ```
- **Shallow copy (referência)**:
  ```python
  nova = lista
  nova.append(5)
  print(lista)       # [1, 2, 3, 5]
  print(nova)        # [1, 2, 3, 5]
  ```

---

Pronto pra colar isso no seu `README.md`? Se quiser, posso te ajudar a organizar os diretórios no repositório ou criar um sumário automático. 😄
