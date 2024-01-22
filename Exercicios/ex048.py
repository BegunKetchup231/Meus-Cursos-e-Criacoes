# Faça um program que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo entre 1 até 500.

soma = 0
contagem = 0

for numeros in range(1, 501):
    if numeros % 2 != 0 and numeros % 3 == 0:
        soma += numeros
        contagem += 1
        
print(f"\033[93mA soma dos {contagem} valores multiplos de 3 e ímpares é de: {soma}\033[0m")
