from datetime import datetime

#transformar string em data: %d/%m/%Y > Y = 2022 y = 22   %H = 24h %I = 12h  %M = Minutos  %h = nome mes
dt_str = '31/05/2022 14:28'
dt = datetime.strptime(dt_str, '%d/%m/%Y %H:%M')

#strftime transformar data
dt = datetime(2022, 5, 31, 20 ,42)
print(dt.strftime('%d/%h/%Y %I:%M'))