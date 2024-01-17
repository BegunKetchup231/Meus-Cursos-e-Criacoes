for oi in range(1 , 6) :
    print("Oi")
print("Fim")


for c in range(6, 0, -1) :
    print(oi)
print("Fim")

#for é a estrutura de repetição
#c é o nome da variável
#in range é o numero e quantidade
for c in range(0, 7, 2) :
    print(c)
print("Fim")

soma = 0
for c in range(0, 4) :
    numero = int(input('Digite um número: '))
    # "soma += n" é o mesmo que "soma = s + n"  
    soma += numero
print(f'A soma de todos os números é de: {soma}')
