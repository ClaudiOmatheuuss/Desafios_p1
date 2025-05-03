# Peça ao usuário para informar idades até que ele digite um valor negativo. Após
# isso, exiba a média das idades informadas (desconsidere o valor negativo no
# cálculo).

num_usuario = 0
idades = []
i = 0

while True:
  num_usuario = int(input(f"Informe a idade{i + 1}: "))
  if num_usuario >= 0:
    idades.append(num_usuario)
  else: 
    break
  i += 1

media_idades = sum(idades)/len(idades)

print("_" * 40 + f"\n Considerando as idades informadas a media delas eh: {media_idades} \n" + "_" * 40)