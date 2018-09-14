'''
'' Exemplos básicos da utilização do python!
'''
print('Olá Mundo!')

## if ternário !!!
print('Olá Mundo' if True else 'Não diga olá mundo') 
print('Olá Mundo' if False else 'Não diga olá mundo')

'''
'' Listas e dicionários
'''
lista = [] # nova lista!
lista.append(1)
print(lista)

lista = ([0]*5) + ([1]*5) # nova lista com 10 posições (5 zeros e 5 ums)
print(lista[5:]) #a partir da posição 5
print(lista[:5]) #até a posição 5 (sem incluí-la))
print(lista[-3:]) #últimos 3

# percorrer listas!
for elemento in lista:
  print(f'elemento: {elemento}')

# ok, com índice
for indice in range(len(lista)):
  print(f'elemento[{indice}]: {lista[indice]}')

dicionario = {'1': 1, '2': 2} # novo dicionario!
print(dicionario)

print(dict.fromkeys([1,2,3],55)) # novo dicionário com valores padrão...

'''
'' List comprehensions
'''
nova_lista = [letra for letra in 'nova lista']
print(nova_lista)

nova_lista = [letra for letra in 'nova lista' if letra != ' ']
print(nova_lista)

pares_ao_quadrado = [nr_par ** 2 for nr_par in range(0,20) if nr_par % 2 == 0]
print(pares_ao_quadrado)

# [0, 2] * [1, 3] = [0, 0, 2, 6]
pares_vezes_impares = [nr_par * nr_impar for nr_par in range(0,4) if nr_par % 2 == 0 for nr_impar in range(0,4) if nr_impar % 2 != 0]
print(pares_vezes_impares)