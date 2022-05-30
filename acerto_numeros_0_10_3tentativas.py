from random import randint

nr_sorteado = randint(0, 10) 

for chance in range (1, 4):
    numero = int(input(f"{chance}ª chance - Digite um numero de 0 a 10: "))
    if nr_sorteado == numero:
        print("Voce acertou! O número é:", nr_sorteado)
        exit()
    else:
        if chance == 3:
            mensagem = 'Inicie um novo jogo!'
            
        else:
            mensagem = 'Tente novamente!'
        print(f"Número errado! {mensagem}")
print(f'Numero sorteado {nr_sorteado}')