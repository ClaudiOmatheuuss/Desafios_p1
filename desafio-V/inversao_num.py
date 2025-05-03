# Escreva um programa que peça ao usuário um número inteiro positivo e use um laço
# para calcular e exibir o número ao contrário.
# a. Exemplo: Entrada: 1234 → Saída: 4321.

lista = list(input("Insira um número inteiro positivo: "))
nova_lista = []
contador = 0

for contador in lista:
  contador = lista.index(contador)

i = contador
while i >= 0:
  nova_lista.append(lista[i])
  i -= 1

b = ""
for num in nova_lista:
  b += num

print(b)