# 5. Faça um programa que leia uma velocidade em km/h e a converta para m/s. Mostre
# o valor original e o valor convertido. (Pesquise como fazer essa conversão.)

print("Bem-vindo(a), ao sistema de conversão \n Opções válidas \n a. km/h \n b. m/s")

opcoes_validas = ["a", "km/h", "b", "m/s"]
medida_escolhida = ""

while (medida_escolhida not in opcoes_validas):
  medida_escolhida = input("Insira a medida do valor original: ")
  velocidade = int(input("Insira o valor original da velocidade: "))

  if (medida_escolhida == "a" or medida_escolhida == "km/h"):
    velocidade_convertida = velocidade * 3.6
    medida_original = " km/h"
    medida_conversao = " m/s"
  elif (medida_escolhida == "b" or medida_escolhida == "m/s"):
    velocidade_convertida = velocidade / 3.6
    medida_original = " m/s"
    medida_conversao = " km/h"
  else:
    print("Opção inválida! Tente novamente.")

print("-" * 45)
print(f"\n Valor original: {velocidade}{medida_original} \n Valor convertido: {velocidade_convertida}{medida_conversao}")