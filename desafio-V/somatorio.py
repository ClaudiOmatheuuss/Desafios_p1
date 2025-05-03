# Escreva um programa que peça um número ao usuário e continue pedindo até
# que ele informe o número 0. Quando isso acontecer, exiba a soma de todos os
# números informados.
print("_" * 40 + "\n Bem vindo(a) ao sistema de somatório \n" + "_" * 40)
num_usuario = int(input("Informe um número qualquer: "))
soma_total = 0

while(num_usuario != 0):
  soma_total = soma_total + num_usuario
  num_usuario = int(input("Informe um número qualquer: "))

print("_" * 40 + f"\n Resultado da soma: {soma_total} \n" + "_" * 40)