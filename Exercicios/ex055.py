# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for pessoas in range(1, 6):
    pesos = float(input(f"Digite o peso da {pessoas}a pessoa: "))

    if pessoas == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos

print(f"O maior peso foi de {maior:.1f}kg!")
print(f"O menor peso foi de {menor:.1f}kg!")