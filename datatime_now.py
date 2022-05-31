from datetime import datetime

antiga = datetime(2000, 11, 28, 14, 30)
agora = datetime.now()

print(f'Hoje é: {agora.date()} e horário: {agora.time()}')
print((agora - antiga).days)