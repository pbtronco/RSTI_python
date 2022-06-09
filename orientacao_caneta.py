#MODELAGEM - POO
#CARACTERISTICAS = ATRIBUTOS
#AÇÕES = MÉTODOS
#ESTADO
from time import sleep


class Caneta:
    cor = None
    modelo = None
    qtd_tinta = 10
    
    def riscar(self):
        if self.qtd_tinta:
            print('Estou riscando')
            self.qtd_tinta -= 1
        else:
            print('Estou sem tinta')

caneta_a = Caneta()
caneta_a.cor = 'Vermelha'
caneta_a.modelo = 'Caneta quadro branco'

print(caneta_a.cor)
print(caneta_a.modelo)
print(f'Quantidade de tinta inicial: {caneta_a.qtd_tinta}')

for i in range(0,12):
    caneta_a.riscar()
    print(f'Quantidade de tinta inicial: {caneta_a.qtd_tinta}')
    sleep(2)