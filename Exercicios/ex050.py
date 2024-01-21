# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
# daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

cor_vermelha = "\033[91m"
cor_reset = "\033[0m"
soma = 0

for numeros in range(1, 7):
    numeros = int(input("Digite um número: "))
    if numeros % 2 == 0:
        soma += numeros
        
print(f"{cor_vermelha}A soma de todos os números pares é de: {soma}{cor_reset}")