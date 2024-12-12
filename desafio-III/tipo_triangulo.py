# 6. Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

prim_lado = int(input("Informe o primeiro lado: "))
seg_lado = int(input("Informe o segundo lado: "))
terc_lado = int(input("Informe o terceiro lado: "))

triangulo = ((prim_lado + seg_lado) > terc_lado) and ((prim_lado + terc_lado) > seg_lado) and ((seg_lado + terc_lado) > prim_lado)

def verifica_triangulo(prim_lado, seg_lado, terc_lado):

    if prim_lado == seg_lado == terc_lado:
        return "Triângulo Equilátero"
    elif prim_lado == seg_lado or prim_lado == terc_lado or seg_lado == terc_lado:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"


print(verifica_triangulo(prim_lado, seg_lado, terc_lado)) if triangulo else print("Não é um triângulo")