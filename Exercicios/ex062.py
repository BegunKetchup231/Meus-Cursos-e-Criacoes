# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

print("Calculadora de Progressão Aritimética")
print("-=-" * 13)
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"{termo} > ", end="")
        termo += razao
        contador += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Fim")
