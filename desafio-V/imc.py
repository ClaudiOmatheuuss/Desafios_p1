# 7. Crie um programa que peça ao usuário seu peso (em quilogramas) e sua altura
# (em metros). O programa deve calcular o Índice de Massa Corporal (IMC) e exibir
# a categoria de peso do usuário com base na tabela abaixo:
# Fórmula do IMC: peso/altura²
# Categorias:
#   a. Abaixo de 18.5: Abaixo do peso
#   b. Entre 18.5 e 24.9: Peso normal
#   c. Entre 25.0 e 29.9: Sobrepeso
#   d. Entre 30.0 e 34.9: Obesidade grau 1
#   e. Entre 35.0 e 39.9: Obesidade grau 2
#   f. 40.0 ou mais: Obesidade grau 3

print("_"*40 + "\n Bem vindo(a), ao nosso sistema de IMC \n" + "_"*40)

peso_usuario = float(input("Digite seu peso em kg): "))
altura_usuario = float(input("Digite sua altura em metros: "))

imc = peso_usuario/altura_usuario**2
print("_"*40)
print(f"Seu IMC é: {imc}")

if(imc < 18.5):
  print("Categoria: Abaixo do peso! \n" + "_"*40)
elif(imc >= 18.5 and imc <= 24.9):
  print("Categoria: Peso normal \n" + "_"*40)
elif(imc >= 25 and imc <= 29.9):
  print("Categoria: Sobrepeso \n" + "_"*40)
elif(imc >= 30 and imc <= 34.9):
  print("Categoria: Obesidade grau 1 \n" + "_"*40)
elif(imc >= 35 and imc <= 39.9):
  print("Categoria: Obesidade grau 2 \n" + "_"*40)
elif(imc >= 40):
  print("Categoria: Obesidade grau 3 \n" + "_"*40)
else:
  print("Peso ou altura inválido(s), reinicie o sistema e tente novamente \n" + "_"*40)
