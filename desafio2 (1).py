from datetime import datetime, date, timedelta

nome = input("Nome: ")
dt_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
#date separada do time .date no final
dt_nascimento = datetime.strptime(dt_nascimento, '%d/%m/%Y').date()

idade = ((date.today() - dt_nascimento) / 365).days

if idade >= 18:
    print(f"{nome} tem {idade} anos, e é MAIOR de idade")
else:
    print(f"{nome} tem {idade} anos, e é MENOR de idade")