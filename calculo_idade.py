nome = input("Digite seu nome: ")
ano = int(input("Digite seu ano de nascimento: "))
data = int(input("Digite em que ano estamos: "))
idade = data - ano

if (idade >= 21):
    print(nome,"você tem", idade,"anos, e é maior de idade!")

else:
    print(nome,"você tem", idade,"anos, e é menor de idade!")