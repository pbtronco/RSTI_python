matriz = [[1,2,3], [4,5,6], [7,8,9]]

somatorio_coluna_0 = 0
somatorio_coluna_1 = 0
somatorio_coluna_2 = 0
    
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'Linha: {linha} Coluna: {coluna} => {matriz[linha][coluna]}')
        if (matriz[linha][coluna] % 2) == 0:
            print(f'O Valor: {matriz[linha][coluna]} é PAR')
        else:
            print(f'O Valor: {matriz[linha][coluna]} é ÍMPAR')
        if coluna == 0:
            somatorio_coluna_0 += matriz[linha][coluna]
        elif coluna == 1:
            somatorio_coluna_1 += matriz[linha][coluna]
        elif coluna == 2:
            somatorio_coluna_2 += matriz[linha][coluna]
            
print(f'Smatório coluna 0: {somatorio_coluna_0}')
print(f'Smatório coluna 1: {somatorio_coluna_1}')
print(f'Smatório coluna 2: {somatorio_coluna_2}')