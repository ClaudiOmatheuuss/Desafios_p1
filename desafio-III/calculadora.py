# 8. Faça um programa que leia 2 números e depois pergunte ao usuário qual operação ele deseja realizar. 
#    Imprima o resultado da operação. O usuário pode escrever uma das seguintes operações: 
#   a) soma   b) subtração c) multiplicação d) divisão e) exponenciação 

print("Bem vindo(a)! :)")
print("-" * 25)
print(" " * 6 + "Calculadora")
print("-" * 25)
print("Insira os dois números desejados para calcular:")
prim_num = float(input("Primeiro número: "))
seg_num = float(input("Segundo número: "))
print("-" * 25)
print("| Operações: \n| a) soma \n| b) subtração \n| c) multiplicação \n| d) divisão \n| e) exponenciação")
print("-" * 25)
operacoes = ["a", "b", "c", "d", "e"] # array com as opções de operação possíveis

# o método lower garante que a string recebida será formatada em letra minuscula, isso garante que não haja erro na hora de por exemplo comparar "A" com "a"
operacao_escolhida = input("Qual operação deseja realizar? ").lower() 
operacao_invalida = operacao_escolhida not in operacoes 

# se o input recebido não corresponder com nenhum elemento no array operacoes, operacao_invalida será True o que desencadeia um loop até que o usuário entre com um valor válido
while operacao_invalida:
    operacao_escolhida = input("Operação não existe, tente novamente! \n \n Escolha a operação desejada e insira a letra correspondente(a, b, c, d ou e): ").lower()
    operacao_invalida = operacao_escolhida not in operacoes  #verifica a entrada ao final de cada iteração do loop

if operacao_escolhida == operacoes[0]: # soma
    print(f"Resultado => {prim_num + seg_num}")
elif operacao_escolhida == operacoes[1]: # subtração
    print(f"Resultado => {prim_num - seg_num}")
elif operacao_escolhida == operacoes[2]: # multiplicação
    print(f"Resultado => {prim_num * seg_num}")
elif operacao_escolhida == operacoes[3]: # divisão
    print(f"Resultado => {prim_num / seg_num}")
else: # exponenciação
    print(f"Resultado => {prim_num ** seg_num}")