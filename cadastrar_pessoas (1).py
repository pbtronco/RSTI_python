pessoas = []
total_pessoas = int(input("Quantas pessoas desejas cadastrar?"))

while len(pessoas) < total_pessoas:
    pessoas.append(input("Nome: "))
print("LISTAGEM DE PESSOAS:")

for pessoa in sorted(pessoas):
    print(pessoa.title())

