from random import randint

nr_sorteado = randint(1, 10) 
numero = int(input("Digite um numero: "))

if nr_sorteado == numero:
    print("Voce acertou! O número é:", nr_sorteado)
else:
    print("Número errado! O número era: ", nr_sorteado)