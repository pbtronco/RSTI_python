nome1 = input("Digite seu nome: ").title()
cupom = input("Digite seu cupom: ").upper().replace(' ',"")

total_compra = float(input("Digite o valor total da compra: "))

if cupom == "CUPOM10":
    cupom1 = total_compra - (total_compra * 0.1)
    print(nome1, "sua compra com o cupom deu: R$", cupom1)
elif cupom == "CUPOM25":
    cupom2 = total_compra - (total_compra * 0.25) 
    print(nome1, "sua compra com o cupom deu: R$", cupom2)
else:
    print("Sua compra sem cupom é igual a: R$", total_compra)