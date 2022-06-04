from time import sleep
import os
from calculadora_ferramentas import soma, subtracao, divisao, multiplicacao
from menu import mostrar_menu, capturar_numeros



opcao = mostrar_menu()

while opcao != 5:
    nr_1, nr_2 = capturar_numeros()
    if opcao == 1:
        print(f'O resultado de {nr_1} + {nr_2} = {soma(nr_1, nr_2)}')
    elif opcao == 2:
        print(f'O resultado de {nr_1} - {nr_2} = {subtracao(nr_1, nr_2)}')
    elif opcao == 3:
        print(f'O resultado de {nr_1} x {nr_2} = {multiplicacao(nr_1, nr_2)}')
    elif opcao == 4:
        print(f'O resultado de {nr_1} / {nr_2} = {divisao(nr_1, nr_2)}')
    else:
        print(f'Opcao inválida')
#tela de espera por 4 segundos
    sleep(4)
#limpar tela acima
    os.system('clear')
    opcao = mostrar_menu()
    
print(">>>>PROGRAMA FINALIZADO<<<<")
