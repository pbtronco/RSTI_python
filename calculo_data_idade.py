from datetime import date, datetime

dt_1 = date(2022, 5, 31)
dt_2 = date(1965, 7, 26)

dt_2 = dt_2.replace(year=1993)

anos = (dt_1 - dt_2) / 365

print(f'Voce tem {anos.days} anos')

hoje = date.today()

print(f'Hoje é: {hoje}')