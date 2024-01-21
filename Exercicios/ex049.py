# Refaça o desafio 009, mostrando a tabuada de um número que o usuário
# escolher. Só que agora utilizando um laço for.

print("Tabuada dos Números!!")

numero = int(input("Digite um número: "))

multiplicacao = 0
print(f"A tabuada do número {numero} é: ")

for quantidade in range(0, 11):
    multiplicacao = quantidade * numero
    print(f"{numero} x {quantidade:2} = {multiplicacao}")
