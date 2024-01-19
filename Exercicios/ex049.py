# Refaça o desafio 009, mostrando a tabuada de um número que o usuário
# escolher. Só que agora utilizando um laço for.

# Pede ao usuário para digitar um número
num = int(input("Digite um número para saber sua tabuada: "))

# Define a multiplicação ao valor de 0
multi = 0

# Print estético da calculadora
print(("-" * 10), "Tábuada do", f"{num}", ("-" * 10))

# Define por quanto o "num" será multiplicado, no caso por 1 até 10
for quant in range (0, 11) :

    # Faz a multiplicação da quantidade pelo número 
    multi = (quant * num) 

    # Mostra na tela o resultado do num x 1, 2 etc até 10...
    print("-+- "f"{num} x {quant:2} = {multi}")

# Print estético
print("-" * 36)
