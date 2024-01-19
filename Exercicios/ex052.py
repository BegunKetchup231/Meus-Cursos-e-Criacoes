# Desenvolva um programa que leia um número inteiro e diga se ele é ou não um número primo

# Pede ao usuário um número inteiro
num = int(input("Digite um número Inteiro: "))

# Define que o total de divisões do num ainda é 0
total = 0 

for c in range(1, num + 1):

    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
        
    else:
        print('\033[31m', end=' ')
    print(f'{c} ', end=' ')
        
print(f'\n\033[mO número {num} foi divisível {total} vezes')
    
# Se o total de divisões do num for 2, divisível por 1 e ele mesmo, ele é definido como primo
if total == 2: 
    print(f'O número {num} é um número Primo!')

else:
    print(f'O número {num} não é um número Primo!')
    