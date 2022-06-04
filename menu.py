def mostrar_menu():
    print("'...............................'")
    print("'+++------ CALCULADORA ------+++'")
    print("'---Escolha a opção desejada:---'")
    print("'     1 - ADIÇÃO                '")
    print("'     2 - SUBTRAÇÃO             '")
    print("'     3 - MULTIPLICAÇÃO         '")
    print("'     4 - DIVISÃO               '")
    print("'     5 - SAIR                  '")
    print("'''''''''''''''''''''''''''''''''")
    return(int(input("Opção:")))
    
def capturar_numeros():
    nr_1 = float(input("Digite o primeiro número: "))
    nr_2 = float(input("Digite o segundo número: "))
    return nr_1, nr_2