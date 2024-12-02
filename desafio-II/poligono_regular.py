#11. Escreva um programa para ler o número de lados de um polígono regular. Calcular e imprimir o seguinte:
#     a. Se o número de lados for igual a 3 imprima TRIÂNGULO
#     b. Se o número de lados for igual a 4 imprima QUADRADO
#     c. Se o número de lados for igual a 5 imprima PENTÁGONO

lados = int(input("Insira a quantidade de lados que tem o polígono: "))

if lados == 3:
    print("TRIÂNGULO")
elif lados == 4:
    print("QUADRADO")
elif lados == 5:
    print("PENTÁGONO")