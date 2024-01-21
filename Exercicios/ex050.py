# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
# daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

color = "033[93m"
resetcolor = "033[0m"
soma = 0

for numeros in range(1, 7):
    numeros = int(input("Digite um número: "))
    if numeros % 2 == 0:
        soma += numeros
        str(soma)
print(f"A soma de todos os números pares é de: {soma}")