# Crie um program que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50.

print("Esses são todos os números pares entre 1 e 50")

for numeros in range(1, 51):
    if numeros % 2 == 0:
        print(numeros)
