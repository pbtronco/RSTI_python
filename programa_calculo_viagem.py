print("Calculo de despesas da viagem")
pessoas = int(input("Digite o numero de pessoas: "))
hospedagem = float(input("Digite o valor da hospedagem: "))
pedagio = float(input("Digite o valor do pedagio: "))
pedagio1 = int(input("Digite o numero de pedágios do percurso: "))
autonomia = float(input("Digite a autononia do carro seu carro: "))
distancia = float(input("Digite a distancia do percurso: "))
gas = float(input("Digite o preco do combustivel:"))
print(40*'-')
#preco da hospedagem
r1 = pessoas * hospedagem
#preco do combustivel por km/l
combustivel = (distancia / autonomia) * gas
#preco dos pedagios
r2 = pedagio * pedagio1
#preco do combustivel + pedagio 
r3 = combustivel + r2
#valor total da hospedagem
r4 = r1 + r2 + r3
print("O valor total da hospedagem para ", pessoas, " pessoas é R$", round(r1, 2))
print("O valor total da gasolina e R$", round(combustivel, 2))
print("O valor total do percurso com os pedagios e R$", round(r3, 2))
print("O valor total da viagem é R$", round(r4, 2))

