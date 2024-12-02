#10.   Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 5544. Devem ser impressas as seguintes mensagens:
#      a. ACESSO PERMITIDO caso a senha seja válida.
#      b. ACESSO NEGADO caso a senha seja inválida.

print("Bem vindo(a) ao nosso sistema, para liberar acesso digite a senha")
entrada_usuario = int(input(""))

if entrada_usuario == 5544:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")