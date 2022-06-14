from datetime import datetime, date

class Pessoa:
    nome = None
    data_nascimento = None
    funcao_profissional = None
    email = None
    telefone = None
    
    def imprimir_cartao_visita(self):
        print('************************************************************')
        print(f'Nome: {self.nome}                                          ')
        print(f'Idade: {((date.today()-self.data_nascimento) / 365).days}  ')
        print(f'Função profissional: {self.funcao_profissional}            ')
        print(f'E-mail: {self.email}                                       ')
        print(f'Telefone: {self.telefone}                                  ')
        print('************************************************************')


pessoas = []

pessoa_a = Pessoa()
pessoa_a.nome = 'Penny Hofstadter'
pessoa_a.data_nascimento = datetime.strptime('30/11/1985', '%d/%m/%Y').date()
pessoa_a.funcao_profissional = 'Atendente Fábrica de Cheesecake'
pessoa_a.email = 'penny@tbbt.com'
pessoa_a.telefone = '55-99999-9999'

pessoa_b = Pessoa()
pessoa_b.nome = 'Pablo Borges Tronco'
pessoa_b.data_nascimento = datetime.strptime('26/07/1993', '%d/%m/%Y').date()
pessoa_b.funcao_profissional = 'Engenheiro Mecânico'
pessoa_b.email = 'pbtronco@hotmail.com'
pessoa_b.telefone = '55-99605-9909'

pessoa_c = Pessoa()
pessoa_c.nome = 'João da Silva'
pessoa_c.data_nascimento = datetime.strptime('25/05/1999', '%d/%m/%Y').date()
pessoa_c.funcao_profissional = 'Jogador de Futebol'
pessoa_c.email = 'joaozinho@hotmail.com'
pessoa_c.telefone = '55-81923-9999'


pessoa_a.imprimir_cartao_visita()
pessoa_b.imprimir_cartao_visita()
pessoa_c.imprimir_cartao_visita()