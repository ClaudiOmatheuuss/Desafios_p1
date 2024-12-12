# 2. Faça um programa que leia dois números e efetua a adição. Se o valor somado for
#    maior que 20, este deverá ser apresentado somando-se a ele 8; 
#    se o valor somado for menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.

prim_num = float(input("Digite o primeiro número: "))
seg_num = float(input("Digite o segundo número: "))

soma = prim_num + seg_num

if soma > 20:
    soma = soma + 8
else:
    soma = soma - 5

print(f"Resultado = {round(soma, 2)}")