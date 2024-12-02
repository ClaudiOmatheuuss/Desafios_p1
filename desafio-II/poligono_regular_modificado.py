# 12. Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
# a. Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
# b. Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

lados = int(input("Insira a quantidade de lados que tem o polígono: "))

if lados == 3:
    print("TRIÂNGULO")
elif lados == 4:
    print("QUADRADO")
elif lados == 5:
    print("PENTÁGONO")
elif lados < 3:
    print("NÃO É UM POLÍGONO")
else: 
    print("POLÍGONO NÃO IDENTIFICADO")