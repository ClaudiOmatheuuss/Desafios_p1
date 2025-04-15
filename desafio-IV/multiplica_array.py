# 9. Crie uma lista contendo os números [1, 3, 5, 7, 9]. Multiplique cada número da lista
# por 2 e armazene os resultados em uma nova lista. Imprima a nova lista.

lista = [1, 3, 5, 7, 9]
nova_lista = []

for numero in lista:
  nova_lista.append(numero*2)

print(nova_lista)