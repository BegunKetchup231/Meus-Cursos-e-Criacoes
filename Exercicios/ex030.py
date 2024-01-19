# Pede para o usuário digitar um número inteiro
numero = int(input('Digite um número inteiro '))

# Verifica se a divisão inteira do número é igual a 0 para ser Par e mostrar na tela
if numero % 2 == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é ÍMPAR')
