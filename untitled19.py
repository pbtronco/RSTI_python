peso_bagagem = float(input("Digite o peso da sua bagagem: "))

if peso_bagagem > 10:
    print("Você paga R$", (peso_bagagem - 10) * 2)