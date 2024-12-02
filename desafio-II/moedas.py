# 7. Crie um programa que leia quanto reais uma pessoa tem na carteira e mostre quantos dólares ela pode comprar com esse dinheiro.
saldo = float(input("Digite quantos reais você tem na carteira: "))

conversao_dol = saldo / 6.04  # conversão em dólares

print(f"Com R${round(saldo, 2)}, você pode comprar US${round(conversao_dol, 2)}.")