#laços de repetição
lista = range(0,30)
for item in lista:
    resto = item % 2
    if resto == 0:
        print("O numero", item, "é PAR")
    else:
        print("O numero", item, "é IMPAR")