"""
Tuplas são muito parecidas com lista. A grande diferença é que, uma vez criada a tupla, ela não pode mais mudar. Ou
seja, nada de acrescentar, remover ou alterar elementos.
Podemos criar Tuplas com (...) (parênteses) ao invés de [...] (colchetes).
"""

primeira_tupla = ("Let's", 'Data', 4, 2.1, False)
print(primeira_tupla)

"""
Outra forma de criar uma Tupla é: basta atribuir valores separados por vírgula. O Python cria a Tupla e armazena todos 
os valores na ordem repassada.
"""

segunda_tupla = 1, 2, 3, 'de oliveira 4'
print(segunda_tupla)
print(type(segunda_tupla))

"""
O acesso ao elemento de uma Tupla é igualzinho na Lista, pelo seu índice, ou seja, a posição do elemento dentro da 
Lista.
Lembrando, mais uma vez, que o primeiro elemento está na posição 0 (zero).
Assim como na Lista, também é possível acessar o último elemento sem saber quantos elementos temos na Tupla. É só 
passar uma posição negativa: começando pelo -1 (menos um).
"""

print(segunda_tupla[0])
print(segunda_tupla[-1])
