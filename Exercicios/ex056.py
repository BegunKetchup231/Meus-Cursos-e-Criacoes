# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo;
# Qual é o nome do homem mais velho;
# Quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadeh = 0
nomemaisvelho = ""
totalmulher20 = 0

for pessoas in range(1 , 5):
    print(f"_____ {pessoas}a Pessoa _____")
    nome = str(input("Digite o nome: ")).upper().strip()
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo, [M/F]: ")).upper().strip()
    somaidade += idade

#   > Segunda forma
#   if pessoas == 1 and sexo in "Mm":
    if pessoas == 1 and sexo == "M":
        maioridadeh = idade
        nomemaisvelho = nome
    if sexo in "M" and idade > maioridadeh:
        maioridadeh = idade
        nomemaisvelho = nome
    if sexo in "F" and idade < 20:
        totalmulher20 += 1

mediaidade = somaidade / 4

print(f"A média de idade do grupo é de {mediaidade} anos")
print(f"O homem mais velho tem {maioridadeh} e se chama {nomemaisvelho}")
print(f"Ao todo são {totalmulher20} mulheres com menos de 20 anos de idade")
