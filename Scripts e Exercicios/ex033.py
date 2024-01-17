# Pede para o usuário digitar 3 números inteiros
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
num3 = int(input('Digite um último número: '))

# Verifica qual dos números é o maior e qual deles é o menor
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

# Printa na tela os 3 números e diz qual é o maior e o menor
print(f'Você digitou {num1}, {num2} e {num3}')
print(f'O menor deles é o {menor} e o maior deles é o {maior}')