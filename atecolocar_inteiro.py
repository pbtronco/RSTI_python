def entrar_inteiro():
    solicitar_inteiro = True
    while True:
        try:
            return int(input('Digite um número inteiro:'))
        except:
            print('Voce deve digitar um numero inteiro!!')
            
numero = entrar_inteiro()
print(f'O dobro de {numero} é {2*numero}')