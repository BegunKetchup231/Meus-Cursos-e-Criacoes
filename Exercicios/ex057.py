# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
# Caso esteja errado, peça a digitação novamente até ter um valor correto

# Maneira 1:

sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0] # < Esse [0] pega só a primeira letra da palavra

while sexo == "F" or sexo == "M":
    print(f"Seu sexo é {sexo.upper()}!!")
    break

else:
    print("Digite uma opção válida")

# Maneira 2:
    
sexo = str(input("Informe seu sexo: ")).upper().strip()

while sexo not in "MmFf":
    sexo = str(input("Dados inválidos, digite novamente! "))
print(f"Sexo {sexo} registrado com sucesso.")