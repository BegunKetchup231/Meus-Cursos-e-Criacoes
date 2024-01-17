# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
# daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.


somapr = 0
somaim = 0

for numero in range(1, 7) :

    numero = int(input("Digite um valor: "))

    if numero % 2 == 0 :

        somapr += numero
    
    else :

        somaim += numero

print(f"A soma de todos os números pares é de: {somapr}")
print(f"A soma de todos os números ímpares é de: {somaim} ")
