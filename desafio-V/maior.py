# Escreva um programa que peça ao usuário 5 números e exiba o maior número
# informado. Dica: Utilize um laço for para coletar os números
qtd_numeros = 4
numeros_usuario = [int(input(f"Digite o número {i + 1}: ")) for i in range(qtd_numeros + 1)]

maior_num = numeros_usuario[0]

j = 0
for j in range(qtd_numeros + 1):
  if maior_num < numeros_usuario[j]:
    maior_num = numeros_usuario[j]

print(f"O maior número dentre os quatro informados é: {maior_num}")