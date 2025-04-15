# 3. Faça um programa que calcule o desconto de um produto em uma loja. Peça o valor
# do produto e o tipo de cliente (aposentado, estudante ou normal).
# a. Se o cliente for aposentado, recebe 15% de desconto.
# b. Se for estudante, recebe 10%.
# c. Caso não seja nenhum dos dois, recebe 5%.

print("Bem-vindo(a), ao sistema da loja \n")
preco_produto = int(input("Insira o preço do produto escolhido: "))

print("Tipos de Cliente \n a. cliente \n b. estudante \n c. nenhum")
tipo_cliente = input("Insira a opção correspondente ao seu tipo de cliente: ")

if (tipo_cliente == "a" or tipo_cliente == "cliente"):
  desconto = preco_produto*(15/100)
elif (tipo_cliente == "b" or tipo_cliente == "estudante"):
  desconto = preco_produto*(10/100)
else:
  desconto = preco_produto*(5/100)

preco_desconto = preco_produto - desconto

print(f"Preço com desconto: {preco_desconto}")