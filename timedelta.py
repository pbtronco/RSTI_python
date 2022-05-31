from datetime import datetime, date, timedelta

assinatura = date(2022, 5, 31)
renovacao = assinatura + timedelta(days=180)


print(f'Data da assinatura: {assinatura}.\nData da renovação: {renovacao}.')
