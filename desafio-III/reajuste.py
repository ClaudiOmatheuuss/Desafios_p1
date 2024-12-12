# 1. Faça um programa que leia o valor de um produto 
#    e imprimir o valor corrigido com o reajuste de 33.33%.

valor_produto = float(input("Insira o valor do produto: "))

reajuste = valor_produto * (1 + 0.3333)

print(f"O valor do produto após o reajuste de 33.33% é {round(reajuste, 2)}")