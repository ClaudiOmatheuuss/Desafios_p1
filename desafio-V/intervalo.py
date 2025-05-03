# Peça ao usuário 7 números e exiba quais deles são maiores que o número 7 e
# menores que o número 77.
numeros_usuario = [int(input(f"Digite o número {i + 1}: ")) for i in range(7)]
numeros_intervalo = []

j = 0
for j in range(7):  # se eh maior que 7 e menor que 77, está no intervalo, entao
  if numeros_usuario[j] > 7 and numeros_usuario[j] < 77: 
    if numeros_usuario[j] not in numeros_intervalo: # evita numeros repetidos
      numeros_intervalo.append(numeros_usuario[j]) # coloca o elemento no fim da lista dos numeros no intervalo
  
if len(numeros_intervalo) != 0: # se ha pelomenos um numero no intervalo
  print("_" * 40 + f"\n Os numeros que estao no intervalo sao: \n {numeros_intervalo} \n" + "_" * 40) 
else:
  print("_" * 40 + "\n Nenhum numero esta no intervalo. \n" + "_" * 40)