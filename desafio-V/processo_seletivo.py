# 3. Crie um programa para avaliar candidatos a um cargo de emprego com base em
# suas habilidades e experiências. O programa deve:
#   a. Perguntar o nome do candidato.
#   b. Solicitar a idade do candidato.
#     i. Se o candidato tiver menos de 18 anos, exiba a mensagem "Idade
#     insuficiente para participar do processo seletivo" e termine o
#     programa.
#   c. Perguntar ao candidato se ele possui experiência na área da vaga (a
#   resposta deve ser "sim" ou "não").
#     i. Caso a resposta seja "sim", pergunte quantos anos de experiência
#     ele possui.
#   1. Se possuir mais de 5 anos de experiência, exiba "Parabéns,
#   você está altamente qualificado!".
#   2. Se possuir de 1 a 5 anos, exiba "Você está qualificado para a
#   vaga."
#   3. Se possuir menos de 1 ano, exiba "Você tem pouca
#   experiência, mas pode participar do processo."
#     ii. Caso a resposta seja "não", pergunte se ele possui algum curso ou
#     certificação na área (responda com "sim" ou "não").
#       1. Se a resposta for "sim", exiba "Você pode participar do
#        processo seletivo com base em sua formação."
#       2. Caso contrário, exiba "Infelizmente, você não atende aos
#       requisitos mínimos para a vaga."

print("_"*40 + "\n Bem vindo(a), ao nosso sistema de candidatura \n" + "_"*40)
print("\n Antes de prosseguir precisaremos de informações como nome e idade")
nome_candidato = input("nome: ")
idade_candidato = int(input("idade: "))

if (idade_candidato < 18): 
  print("Idade insuficiente para participar do processo seletivo")
else: 
  experiencia_candidato = ""
  respostas_validas = ["sim", "nao"]
  resposta_invalida_xp = True
  
  while(resposta_invalida_xp):
    experiencia_candidato = input("Possui experiência na área da vaga(sim ou nao): ")
    resposta_invalida_xp = experiencia_candidato not in respostas_validas 
    if (resposta_invalida_xp):
      print("Você deve responder com (sim ou não), tente novamente! \n" + "_"*40)
    elif (experiencia_candidato == "sim"):
      experiencia_tempo = -1
      while (experiencia_tempo <= -1):
        experiencia_tempo = int(input("Quantos anos de experiência você possui ? \n"))
        if (experiencia_tempo > 5):
          print("Parabéns, você está altamente qualificado!\n" + "_"*40)
        elif (experiencia_tempo >= 1 and experiencia_tempo <= 5):
          print("Parabéns, você está qualificado para a vaga.\n" + "_"*40)
        elif (experiencia_tempo < 1 and experiencia_tempo > -1):
          print("Você tem pouca experiência, mas pode participar do processo.\n" + "_"*40)
        else:
          print("Anos de experiência inválido, tente novamente! DICA: deve ser um número maior ou igual a 0\n" + "_"*40)
    else:
      certificacao_candidato = ""
      resposta_invalida_cert = True 
      while(resposta_invalida_cert):
       certificacao_candidato = input("Possui algum curso ou certificação na área (responda com sim ou não).")
       resposta_invalida_cert = certificacao_candidato not in respostas_validas 
      if (resposta_invalida_cert):
        print("Você deve responder com (sim ou não), tente novamente!")
      elif (certificacao_candidato == "sim"):
        print("Você pode participar do processo seletivo com base em sua formação.\n" + "_"*40)
      else:
        print("Infelizmente, você não atende aos requisitos mínimos para a vaga.\n" + "_"*40)