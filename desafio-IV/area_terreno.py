# 2) Faça um programa que peça ao usuário 
#   a largura e o comprimento de um terreno retangular 
#   e calcule a área e o perímetro desse terreno.

largura = float(input("Insira a largura do terreno: \n"))
comprimento = float(input("Insira o comprimento do terreno: \n"))

area = largura * comprimento
perimetro = largura * 2 + comprimento * 2

print("_"*40 + f"\n Dado a largura({largura}) e o comprimento({comprimento}) do terremos, temos:\n\n area = {area} m^2 \n perimetro = {perimetro} m\n" + "_"*40)