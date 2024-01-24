# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

print("Digite o ano de nascimento de 7 pessoas")

anohj = 2024
maior = 0
menor = 0

for anonasci in range(1,8):
    anodela = int(input(f"Pessoa {anonasci}: "))
    if anohj - anodela >= 21:
        maior += 1
    else:
        menor += 1

print(f"{maior} pessoas já são de maiores")
print(f"{menor} pessoas são de menores")