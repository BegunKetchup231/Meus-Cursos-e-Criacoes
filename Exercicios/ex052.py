# Desenvolva um programa que leia um número inteiro e diga se ele é ou não um número primo

numero = int(input("Digite um número inteiro: "))

quantidade = 0
for loop in range(1, numero + 1):
    if numero % loop == 0:
        quantidade += 1

if quantidade > 2:
    print(f"\033[91mO número {numero} não é primo!\033[0m")
else:
    print(f"\033[92mO número {numero} é Primo!\033[0m")

print(f"\033[95mO número {numero} tem um total de {quantidade} divisores\033[0m")
