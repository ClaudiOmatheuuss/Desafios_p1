# 8. Escreva um programa que pergunte ao usuário qual número inteiro ele deseja para sua
# tabuada e imprima a tabuada do número escolhido, de 1 a 10.
print("_"*40 + "\n Bem vindo(a), ao nosso sistema de tabuada \n" + "_"*40)

numero_escolhido = int(input("Escolha um número inteiro qualquer: "))
tabuada = [
  numero_escolhido * 1, 
  numero_escolhido * 2, 
  numero_escolhido * 3, 
  numero_escolhido * 4, 
  numero_escolhido * 5,
  numero_escolhido * 6,
  numero_escolhido * 7, 
  numero_escolhido * 8,
  numero_escolhido * 9,
  numero_escolhido * 10
]

print(f"\n A tabuada do número({numero_escolhido}) seria:")
for n in tabuada: print(n)

print("_"*40)