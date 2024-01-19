# Pede ao usuário digitar 2 números aleatórios
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

# Se o número 1 for maior que o 2, o número 1 é o maior
if num1 > num2 :
    print(f'O {num1} é o Maior')

# Se o número 1 é menor que o 2, o número 2 é o maior
elif num1 < num2 :
    print(f'O {num2} é o Maior')

# Se o número 1 e 2 são iguals, retorna que os mesmos são iguais
else :
    print(f'Os números {num1} e {num2} são Iguais!!')