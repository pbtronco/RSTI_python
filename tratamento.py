try:
    numero1 = int(input("Digite um numero:"))
    numero2 = int(input("Digite um numero:"))
    print(f'{numero1} / {numero2} = {numero1/numero2}')

except ZeroDivisionError:
    print("Você não pode dividir um número por ZERO")
except:
    print("Erro ao efetuar a divisão")
else:
    print("Todas entradas estão corretas, processamento OK")
finally:
    print("Vou sempre excutar")