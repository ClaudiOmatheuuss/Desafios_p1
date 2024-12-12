# 9. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#    a) "Telefonou para a vítima?" b) "Esteve no local do crime?"
#    c) “Mora perto da vítima?"  d) "Devia para a vítima?" e) "Já trabalhou com a vítima?" 

#    A resposta do usuário deve ser “sim” ou “nao”. 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = {
    1: "Telefonou para a vítima? ", 
    2: "Esteve no local do crime? ", 
    3: "Mora perto da vítima? ", 
    4: "Devia para a vítima? ", 
    5: "Já trabalhou com a vítima? "
}
respostas_validas = ["sim", "não", "nao"]

def resposta_invalida(resposta, pergunta_feita): # verifica se é resposta válida
    while resposta not in respostas_validas:
        resposta = input(pergunta_feita).lower()
    return resposta

def verifica_respostas(): # faz pergunta e as verifica para receber o valor esperado como resposta: sim ou não
    respostas = {}
    for chave, pergunta in perguntas.items():
        resposta = input(pergunta).lower()
        resposta = resposta_invalida(resposta, pergunta)  # Verifica se a resposta é válida
        respostas[chave] = resposta  # Armazena a resposta
    
    return respostas

def classificar_participacao(respostas): # faz somatório das respostas positivas e classifica o entrevistado
    respostas_positivas = 0
    for resposta in respostas.values():
        if resposta.lower() == "sim":
            respostas_positivas += 1

    if respostas_positivas == 2:
        return "Suspeita"
    elif (respostas_positivas == 3) or (respostas_positivas == 4):
        return "Cúmplice"
    elif respostas_positivas == 5:
        return "Assassino"
    else:
        return "Inocente"

respostas = verifica_respostas()
classificacao = classificar_participacao(respostas)

print(f"Classificação: {classificacao}")