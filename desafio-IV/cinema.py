# 6. Faça um programa para um cinema que peça:
#   a. Idade do espectador
#   b. Dia da semana
#   c. E calcule o preço do ingresso seguindo as regras:
#   d. Segunda a quinta: R$ 30,00
#   e. Sexta a domingo: R$ 40,00
#   f. Aplique essas outras regras:
#     i. Menores de 12 anos: 50% de desconto
#     ii. Maiores de 60 anos: 40% de desconto

print("_"*40 + "\n Bem vindo(a), ao nosso sistema \n" + "_"*40)
idade = -1
dia = ""
idade_invalida = True

while (idade_invalida):
  idade = int(input("Informe-nos sua idade: "))
  idade_invalida = idade < 0 or idade > 150
  
  if (idade_invalida):
    print("Idade Inválida, tente novamente!")

print("_"*40 + f"\n Certo, temos sessões em todos os dias da semana \n" + "\n 1 segunda \n 2 terça \n 3 quarta \n 4 quinta \n 5 sexta \n 6 sábado \n 7 domingo \n" + "_"*40)
dias_validos = [1, 2, 3, 4, 5, 6, 7]

while (dia not in dias_validos):
  dia = int(input("Dia da semana(1, 2, 3, 4, 5, 6, 7): "))
  if (dia not in dias_validos):
    print("Dia inválido, tente novamente!")
  else:
    if (dia >= 1 and dia <= 4):
      ingresso_dia = 30
    else:
      ingresso_dia = 40

if (idade > 12 and idade <= 60):
  preco_total = ingresso_dia - (ingresso_dia * 0.5)
else: 
  preco_total = ingresso_dia - (ingresso_dia * 0.4)

print(f"\n Valor total do ingresso: {preco_total} \n" + "_"*40)