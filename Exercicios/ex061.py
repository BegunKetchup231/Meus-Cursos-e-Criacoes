# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. 

print("Calculadora de Progressão Aritimética")
print("-=-" * 13)
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiro
contador = 1

while contador <= 10:
    print(f"{termo} > ", end="")
    termo += razao
    contador += 1
print("FIM")
