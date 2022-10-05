"""
Uma lista em Python pode conter zero ou mais elementos de qualquer tipo. A lista armazena os valores numa ordem,
começando com o índice 0. Para criar uma lista, basta definir os elementos dentro de [...] (colchetes).
O acesso ao elemento de uma lista se dá pelo seu índice, ou seja, a posição do elemento dentro da lista. Lembrando que
o primeiro elemento está na posição 0 (zero).
"""

primeira_lista = ["Let's Data", 4, 2.1, False]
print(primeira_lista[0])

"""
Uma característica muito legal em Python é a possibilidade de acessar o último elemento  sem saber quantos elementos 
temos na lista. É só passar uma posição negativa: começando pelo -1 (menos um).
"""

print(primeira_lista[-1])
print(primeira_lista[-2])

"""
Para saber a quantidade de elementos de uma lista, utilizamos a função len().
"""

print(len(primeira_lista))

"""
Uma outra característica é que podemos ter repetições de elementos, sem problema nenhum.
"""

segunda_lista = [1, 1, 'repetido', 'repetido']
print(segunda_lista)

"""
Para adicionar elementos numa lista, podemos utilizar o método append().
"""

terceira_lista = ['1° elemento']
print(terceira_lista)

terceira_lista.append('2° elemento')
print(terceira_lista)

"""
Para remover elementos, é um pouquinho diferente (inclusive de outras linguagens), então, muita atenção: utilizamos o 
comando del, passando a posição do elemento a ser removido.
"""

del terceira_lista[0]
print(terceira_lista)

"""
Temos outra opção para remover, utilizando o método remove().
Para isso, temos que passar o elemento que queremos remover, e não a posição.
"""

terceira_lista.remove('2° elemento')
print(terceira_lista)

"""
Para alterar um valor, basta atribuir um novo valor na posição que se quer substituir.
"""

terceira_lista = ["Let's", 'Data', '4tw']
print(terceira_lista)

terceira_lista[2] = 'ftw'
print(terceira_lista)

"""
Uma Última coisinha: você sabia que, em Python, as strings também se comportam como lista?
Temos como acessar os caracteres de uma string pela posição como se fosse uma lista.
"""

str_lets_data = "Let's Data"
print(str_lets_data)
print(str_lets_data[6])
