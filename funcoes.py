from caixa_ferramenta import falador, somar, multiplicar, exponencial, tela_inicio

falador(110,'GREMIO')

tela_inicio()

print('Multiplicação:', multiplicar(3,9))
#definir nr_2 = 1 caso não coloque nada(multiplicação)
print('Multiplicação:', multiplicar(9,))
print('Multiplicação:', multiplicar(2000,5000))

resultado1 = somar(nr_1=8, nr_2=10)
resultado2 = somar(nr_1=1000, nr_2=123)
resultado3 = somar(5000,600000)
#definir nr_2 = 0 caso o usuário não coloque nada(soma)
resultado4 = somar(100,)

print('Exponencial: ', exponencial(2,3))


print('Somar:', resultado1)
print('Somar:', resultado2)
print('Somar:', resultado3)
print('Somar:', resultado4)
