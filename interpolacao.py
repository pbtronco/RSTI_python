#interpolacao
nome = 'Pablo'
str_1 = 'Ola ' +nome+ ' seja bem-vindo!'
print(str_1)

str_2 = 'Ola %s seja bem-vindo!' % nome
print(str_2)

#tupla > é o que fica entre parênteses
# %s = String     %d = Numérico
idade = 29
str_3 = 'Ola %s seja bem vindo! Voce tem %d anos' % (nome, idade)
print(str_3)

# .format = melhor jeito
str_4 = 'Ola {var1} seja bem vindo! Voce tem {var2} anos' .format(var1=nome, var2=idade)
print(str_4)

str_5 = 'Ola {nome} seja bem vindo! Voce tem {idade} anos' .format(nome=nome, idade=idade)
print(str_5)

# f = format 
str_6 = f'Ola {nome} seja bem vindo. Você tem {idade + idade} anos'
print(str_6)