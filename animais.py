#class definir com letra maiuscula ex: VendaProduto
class Cachorro:
    nome = None
    raca = None
    tamanho = None
    pelo = None
    status = 'ACORDADO'
    fome = 10
    
    def escrever_quem_sou(self):
        print(f'Olá, eu sou {self.nome}, sou da raça {self.raca}, e estou {self.status.title()}.')
    
    def dormir(self):
        if self.status == 'ACORDADO':
            self.status = 'DORMINDO'
            print('Agora estou iniciando o ZZZzzzzZZZzzZ!')
        else:
            print('ZzzzZZZzzZZzz!')
            
    def acordar(self):
        if self.status == 'DORMINDO':
            self.status = 'ACORDADO'
            print('Acordei!!!!')
        else:
            print('Já estou acordado!!')
            
    def comer(self):
        if self.status == 'ACORDADO':
            if self.fome < 10:
                print('Estou comendo!')
                self.fome += 1
        else:
            print('ZZZZzzzZZZzz')
            
    def correr(self):
        if self.status == 'ACORDADO':
            if self.fome > 0:
                print('Estou correndo!')
                self.fome -= 1
            else:
                print('Não posso mais corer')
        else:
            print('ZzzzZzzZZz')
    
    def latir(self):
        if self.status == 'ACORDADO':
            print('Au Au Au')
        else:
            print('ZzzZzZzZZzz')