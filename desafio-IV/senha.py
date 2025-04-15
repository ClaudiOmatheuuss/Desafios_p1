# 7. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
usuarios_registrados = {
  "admin": "admin", 
  "claudio": "claudio123"
}

print("_"*40 + "\n Bem vindo(a), ao nosso sistema \n" + "_"*40)

print("Informe o seu nome de usuário e senha abaixo")
usuario = ""
senha = ""
usuario_invalido = True
senha_invalida = True

while(usuario_invalido):
  usuario = input("Nome de usuário: ")
  usuario_invalido = usuario not in usuarios_registrados
  
  if (usuario_invalido): 
    print("Nome de usuário não existe, tente novamente!")
  else:
    while(senha_invalida):
      senha = input("Senha: ")
      senha_invalida = usuarios_registrados[usuario] != senha

      if (senha_invalida):
        print("Senha inválida, tente novamente!")
      else: 
        print("_" * 45 + "\n Acesso permitido! :) \n" + "_" * 45)