# 1) Faça um programa que leia três números inteiros e informe:
#   a. A soma de todos os números.
#   b. O produto de todos os números.
#   c. A média aritmética dos números.
print("Bem-vindo(a), insira três números inteiros \n")
prim_num = int(input("Primeiro número inteiro: "))
seg_num = int(input("Segundo número inteiro: "))
terc_num = int(input("Terceiro número inteiro: "))

soma = prim_num + seg_num + terc_num
produto = prim_num * seg_num * terc_num
media = round(soma/3, 2)

print("_"*40 + f"\n Os resultados são:\n\n soma = {soma} \n produto = {produto} \n média aritmética = {media} \n" + "_"*40)