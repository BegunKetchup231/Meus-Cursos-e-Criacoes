# Desenvolva um programa que leia o primeiro termo e a razão de uma PA e no final, mostre os 10 primeiros termos dessa progressão

print("10 Primeiros termos da PA")

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a Razão da PA: "))

#10 termo
decimo = primeiro + (10 - 1) * razao

print(f"\033[95mOs 10 primeiros termos da PA são:\033[0m")
for termos in range(primeiro, decimo + 1, razao):
    print(f"\033[93m{termos}\033[0m", end=" ")