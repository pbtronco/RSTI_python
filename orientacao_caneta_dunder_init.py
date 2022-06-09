#MODELAGEM - POO
#CARACTERISTICAS = ATRIBUTOS
#AÇÕES = MÉTODOS
#ESTADO
from time import sleep


class Caneta:
    cor = None
    modelo = None
    qtd_tinta = 10
    
    def __init__(self, cor = None, modelo = None):
        self.cor = cor
        self.modelo = modelo
        self.qtd_tinta = 10
    
    def riscar(self):
        if self.qtd_tinta:
            print('Estou riscando ___ 🖋')
            self.qtd_tinta -= 1
        else:
            print('Estou sem tinta')

caneta_a = Caneta(cor='Vermelha', modelo = 'Quadro Branco')
print(caneta_a.cor)
print(caneta_a.modelo)
caneta_a.riscar()
print('Qtd tinta atual', caneta_a.qtd_tinta)
