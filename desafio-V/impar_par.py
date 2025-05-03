#  Escreva um programa que peça ao usuário um número inteiro e diga se ele é par ou ímpar
num_usuario = int(input("Informe o número desejado: "))
ehPar = (num_usuario % 2) == 0

if (ehPar):
  print("_" * 40 + f"\n O número inteiro informado({num_usuario}) é par. \n" + "_" * 40)
else:
  print("_" * 40 + f"\n O número inteiro informado({num_usuario}) é ímpar. \n" + "_" * 40)