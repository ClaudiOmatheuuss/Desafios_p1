# 10. Numa eleição existem três candidatos:
#   a. João, numero 10,
#   b. Maria numero 15, 
#   c. Pedro numero 55.
# Faça um programa que peça o número total de eleitores que vão votar. Em
# seguida peça para cada eleitor votar e ao final mostrar o número de votos de
# cada candidato.

print("_"*40 + "\n Bem vindo(a), ao nosso sistema de votação \n" + "_"*40)

qtd_eleitores = int(input("Qual o número total de eleitores que vão votar: "))
votos = []
for i in range(qtd_eleitores):
  print("_"*40 + "\n Bem vindo(a), ao nosso sistema de votação, eleitor \n")
  voto_eleitor = int(input("Digite o número que corresponde a seu candidato: "))

  votos.append(voto_eleitor)

print("_"*40)
print(f"Sessão concluída \n João(10): {votos.count(10)} votos \n Maria(15): {votos.count(15)} votos \n João(55): {votos.count(55)} votos")
print("_"*40)