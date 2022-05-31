from datetime import date
#data = yyyy-mm-dd

data_nascimento = date(1993, 7, 26)
hoje = date.today()
hoje = hoje.replace(day = hoje.day-1)

print(f'Voce nasceu em {data_nascimento}')
print(hoje)

