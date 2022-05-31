from random import randint
nivel = input('Informe o nível: \n [F] - Fácil \n [D] - Difícil \n')

if nivel.upper() == "F":
    qtd_chances = 5
elif nivel.upper() == "D":
    qtd_chances = 2
else:
    print(f' {nivel} é uma opção inválida!')
    exit()
    
nr_sorteado = randint(0, 10) 

for chance in range (1, qtd_chances+1):
    numero = int(input(f"{chance}ª chance - Digite um numero de 0 a 10: "))
    if nr_sorteado == numero:
        print("Voce acertou! O número é:", nr_sorteado)
        exit()
    else:
        if chance == qtd_chances:
            mensagem = 'Inicie um novo jogo!'
            
        else:
            mensagem = 'Tente novamente!'
        print(f"Número errado! {mensagem}")
print(f'Numero sorteado {nr_sorteado}')