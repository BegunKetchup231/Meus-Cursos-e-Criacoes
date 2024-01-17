# Pede ao usuário para digitar um número inteiro
num = int(input('Digite um número inteiro: '))

# Pergunta para qual base de conversão ele quer converter esse número
print('Escolha como você quer converter: ')
print('1 - Para Binário')
print('2 - Para Octal')
print('3 - Para Hexadecimal')

# Induz o úsuário a escolher 1, 2 ou 3
escolha = int(input('Escolha a opção: '))

# Converte o número para binário, octal, e hexadecimal
binario = bin(num)
octal = oct(num)
hexa = hex(num)

# Retorna com o número convertido dependendo da escolha do usuário
if escolha == 1 :
    print(f'Em Binário o número {num} fica: {binario[2:]}.')
elif escolha == 2 :
    print(f'Em Octal o número {num} fica: {octal[2:]}.')
elif escolha == 3 :
    print(f'Em Hexadecimal o número {num} fica: {hexa[2:]}.')
else :
    print('Por favor escolha uma opção válida!!')