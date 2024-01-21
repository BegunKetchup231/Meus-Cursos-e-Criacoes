# Faça um program que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo entre 1 até 500.

soma = 0

for numeros in range(1, 501):
    if numeros % 2 != 0 and numeros % 3 ==0:
        soma += numeros

print("A soma de todos os números é de:")
print(soma)
 