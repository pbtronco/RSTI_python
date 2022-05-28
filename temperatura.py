meses = [
    {'mes':'janeiro', 'temperatura': 37.5},
    {'mes':'fevereiro', 'temperatura': 37.5},
    {'mes':'marco', 'temperatura': 25.0},
    {'mes':'abril', 'temperatura': 22.0},
    {'mes':'maio', 'temperatura': 21.0},
    {'mes':'junho', 'temperatura': 15.5},
    {'mes':'julho', 'temperatura': 12.5},
    {'mes':'agosto', 'temperatura': 20.5},
    {'mes':'setembro', 'temperatura': 25.5},
    {'mes':'outubro', 'temperatura': 27.5},
    {'mes':'novembro', 'temperatura': 32},
    {'mes':'dezembro', 'temperatura': 35},
]
soma_temperaturas = 0
for mes in meses:
    soma_temperaturas += mes.get('temperatura')
    
    if mes.get('temperatura') < 17:
        sensacao = 'Frio'
    else:
        sensacao = 'Calor'
    print(mes.get('mes'),":", mes.get('temperatura'), "°C Sensação Térmica:", sensacao)
    
print("Media do ano:", round(soma_temperaturas / 12, 2), "°C")

