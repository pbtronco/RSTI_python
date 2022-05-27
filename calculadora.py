a = float(input("Digite o numero 1: "))
b = float(input("Digite o numero 2: "))
c = int(input("Digte 1 para adição, 2 para subtração, 3 para divisão, 4 para multiplicação: "))
if c == 1:
    r1 = a + b
    print('A soma é:', r1)
if c == 2:
    r2 = a - b
    print('A subtracao é:', r2)
if c == 3:
    r3 = a / b
    print('A divisao é:', r3)
if c == 4:
    r4 = a * b
    print('A multiplicacao é:', r4)
if c > 4:
    print("erro")
    