# 8. Faça um programa que leia um número do teclado e escreva na tela se o número é menor, igual ou maior que zero.
numero = float(input("Digite um número: "))

if numero == 0:
    print(f"{numero}, é um número igual a 0.")
elif numero > 0:
    print(f"{numero}, é um número maior que 0.")
else: 
    print(f"{numero}, é um número menor que 0.")