# Faça um programa que leia um número qualquer e mostre o seu fatorial.

print(f"\033[1;93mCalculadora de Fatorial!\033[0m")
numero = int(input("Digite um número: "))

contador = numero
fatorial = 1

print("-=-" * 10)
print(f"\033[94mO fatorial do número {numero} é:\033[0m")
print("-=-" * 10)
while contador > 0:
    print(f"{contador}", end=" ")
    print("x " if contador > 1 else "= ", end="")
    fatorial *= contador
    contador -= 1

print(f"\033[92m{fatorial}\033[0m")
print("-=-" * 10)

# IF dentro do Print
# print("x " if contador > 1 else f"= ", end="")
