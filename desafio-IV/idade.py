# 4. Faça um programa que leia a idade de uma pessoa e informe a categoria:
# a. "Infantil" para idades até 12 anos.
# b. "Adolescente" para idades entre 13 e 17 anos.
# c. "Adulto" para idades de 18 a 59 anos.
# d. "Idoso" para idades a partir de 60 anos.

print("Bem-vindo(a) \n")
idade = -1

while (idade < 0 or idade > 150):
  idade = int(input("Insira a sua idade: "))

  if (idade >= 0 and idade <= 12):
    print(f"Segundo sua idade({idade} anos) você se encaixa na categoria: Infantil")
  elif (idade >= 13 and idade <= 17):
    print(f"Segundo sua idade({idade} anos) você se encaixa na categoria: Adolescente")
  elif (idade >= 18 and idade <= 59):
    categoria = "Adulto"
    print(f"Segundo sua idade({idade} anos) você se encaixa na categoria: Adulto")
  elif (idade >= 60 and idade <= 150):
    print(f"Segundo sua idade({idade} anos) você se encaixa na categoria: Idoso")
  else:
    print("Idade invalida tente novamente")