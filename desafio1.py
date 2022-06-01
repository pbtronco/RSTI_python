from datetime import datetime, date, timedelta

dt_1 = date(2022, 5, 31)
dt_2 = date(2022, 12, 31)

#A) Que dia caira a dt_1 + 180 dias?
nova_data = dt_1 + timedelta(days=180)
print(f"Cairá dia: {nova_data.strftime('%d/%h/%Y')}")

#B) Quantos dias faltam para o reveillon
dias_reveillon = (dt_2 - dt_1).days
print(f"Faltam {dias_reveillon} dias para o reveillon de 2022/2023")

