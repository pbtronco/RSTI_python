#gerar numeros randomicos
from random import randint

nr_sorteado = randint(1, 90) 
print(nr_sorteado)

ls = [8,15,20,80,90,3]
if nr_sorteado in ls:
    print('O número esta na lista!')
else:
    print('O número não está na lista!')
    
#gerar nomes aleatórios
from random import choice

alunos = ['Leandro', 'Mateus', 'Julia', 'Bernardo', 'Lorenzo', 'Raphael', 'Padoin', 'Pablo', 'Victor', 'Davi', 'Gabriel', 'Pablo', 'Thiago', 'Heydrian', 'Marcelo']

sorteado = choice(alunos)

print(sorteado)
