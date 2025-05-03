# Crie um programa que exiba a tabuada de um número informado pelo usuário
print("_"*40 + "\n Bem vindo(a), ao nosso sistema de Calculadora \n" + "_"*40)
num_usuario = int(input("Informe o número desejado: "))

tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

for i in range(len(tabuada)): 
  tabuada[i] *= num_usuario
  i += 1

print(f"Tabuada do numero informado: \n {tabuada} \n" + "_" * 40)