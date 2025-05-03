# 1. Crie um jogo de adivinhação onde o usuário deve acertar um número entre 1 e 10.
# Dê dicas como "Maior" ou "Menor" até que ele acerte. (use o comando while)
import random

num_aleatorio = random.randint(1, 10)
resposta_usuario = 0

print("_"*40 + "\n Bem vindo(a), ao jogo de adivinhação \n" + "_"*40)
while(num_aleatorio != resposta_usuario):
  resposta_usuario = int(input("Digite um número inteiro de 1 a 10: "))
  eh_maior = resposta_usuario > num_aleatorio

  if(resposta_usuario < 1 or resposta_usuario > 10):
    print("Número inválido, tente novamente! \n" + "_"*40)
  elif(eh_maior):
    print("Menor \n" + "_"*40)
  else:
    print("Maior \n" + "_"*40)

print(f"\n Parabéns, você acertou! \n O número correto é: {num_aleatorio} \n" + "_"*40)