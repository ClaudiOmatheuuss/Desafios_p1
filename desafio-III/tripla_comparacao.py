# 3. Faça um programa que receba três inteiros e diga qual deles é o maior e qual o menor.

pri_num = int(input("Insira o primeiro número: "))
seg_num = int(input("Insira o segundo número: "))
ter_num = int(input("Insira o terceiro número: "))

numeros = [pri_num, seg_num, ter_num]
numeros.sort()

print(f"\n O maior número é {numeros[2]} \n O menor número é {numeros[0]}")