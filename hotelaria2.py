#aplicativo para hotelaria
#standard: ADULTO: R$120.00  CRIANÇA: R$60.00
#luxo: ADULTO: R$180.00  CRIANÇA: R$90.00
#qtd_adulto / qtd_criancas
#frigobar: R$ ????
#Tipo da Hospedagem, total de adultos, total de crianças
#data_checkin / data_checkout
#a vista -15%(-0.15) a prazo +5% (+0.5)
from datetime import datetime, date, timedelta

print("HOTEL RSTI")
tabela_precos = {
    'standard': {'adulto': 120, 'crianca': 60},
    'luxo': {'adulto': 180, 'crianca': 90}
}
standard_adulto = tabela_precos['standard']['adulto']
standard_crianca = tabela_precos['standard']['crianca']
luxo_adulto = tabela_precos['luxo']['adulto']
luxo_crianca = tabela_precos['luxo']['crianca']

print(f"Standard Adulto:R$ {standard_adulto}\nStandard Criança:R$ {standard_crianca}\nLuxo Adulto:R$ {luxo_adulto}\nLuxo Criança:R$ {luxo_crianca}")
tipo_hospedagem = input("Tipo de Hospedagem: [standard] ou [luxo]").lower()

qtd_adultos = int(input("Quantidade de adultos: "))
qtd_criancas = int(input("Quantidade de crianças: "))

dt_checkin = datetime.strptime(input("Data do Check-in (dd/mm/aaaa): "), '%d/%m/%Y').date()
dt_checkout = datetime.strptime(input("Data do Check-out (dd/mm/aaaa): "), '%d/%m/%Y').date()

qtd_dias_hospedagem = (dt_checkout - dt_checkin).days

valor_frigobar = float(input("Digite o valor do frigobar: "))

valor_total_adultos = qtd_adultos * qtd_dias_hospedagem * tabela_precos.get(tipo_hospedagem).get('adulto')
valor_total_criancas = qtd_criancas * qtd_dias_hospedagem * tabela_precos.get(tipo_hospedagem).get('crianca')
valor_total_hospedagem_pessoas = valor_total_adultos + valor_total_criancas
valor_total = valor_total_hospedagem_pessoas + valor_frigobar

print("--------------------------TOTAL DA CONTA-----------------------------------")
print(f"Você contratou o plano {tipo_hospedagem.upper()}, por {qtd_dias_hospedagem} dias:")
print(f"Hóspedes:\n{qtd_adultos} Adultos e Valor: R${valor_total_adultos}\n{qtd_criancas} Crianças e Valor: R${valor_total_criancas}")
print(f"O preço da sua hospedagem é: R${valor_total_hospedagem_pessoas}\nO preço do frigobar é: R${valor_frigobar}\nPreço Total da Hospedagem: {valor_total}")
print("---------------------------------------------------------------------------")
forma_pagamento = int(input("Qual a forma de pagamento:\n[1] À vista (15% de desconto):\n[2] À prazo (5% de acréscimo): "))
print("---------------------------------------------------------------------------")
if forma_pagamento == 1:
    avista = valor_total * 0.15
    valor_pagamento = valor_total - avista
    print(f'PREÇO TOTAL À VISTA: R${valor_pagamento}')
elif forma_pagamento == 2:
    prazo = valor_total * 0.05
    valor_pagamento = valor_total + prazo
    print(f'PREÇO TOTAL À PRAZO: R${valor_pagamento}')
else:
    valor_pagamento = valor_total
    print(f'VALOR TOTAL: R${valor_pagamento}')