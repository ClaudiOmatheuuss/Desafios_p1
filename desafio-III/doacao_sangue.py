# 4. Para doar sangue é necessário ter entre 18 e 67 anos. 
#    Faça um aplicativo que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não. 
#    Use alguns dos operadores lógicos OU (or) e E (and).

idade_usuario = int(input("Digite a sua idade(apenas número): \n"))

if idade_usuario >= 18 and idade_usuario <= 67:
    print("Você pode doar sangue")
else:
    print("Você NÃO pode doar sangue")