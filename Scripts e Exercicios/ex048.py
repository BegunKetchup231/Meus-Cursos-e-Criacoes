# Faça um program que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo entre 1 até 500.

contador = 0
soma = 0

for numero in range (1, 501, 2) :
    
    if numero % 3 == 0 :
        
        contador = contador + 1
        soma = soma + numero
        
print(f"A soma entre todos os {contador} valores é de: {soma}", end=" ")