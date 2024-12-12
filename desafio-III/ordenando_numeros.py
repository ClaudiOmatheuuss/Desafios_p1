# 5. Faça um programa que leia três números e mostre-os em ordem decrescente.

pri_num = float(input("Insira o primeiro número: "))
seg_num = float(input("Insira o segundo número: "))
ter_num = float(input("Insira o terceiro número: "))

numeros = [pri_num, seg_num, ter_num]
numeros.sort()
numeros.reverse()

print("A lista final é:")
for numero in numeros:
    print(numero)