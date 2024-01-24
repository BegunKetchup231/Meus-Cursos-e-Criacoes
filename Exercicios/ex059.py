# Crie um programa que leia 2 valores, e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

from time import sleep

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

escolhauser = 0

print("Escolha o que você quer fazer...")
while escolhauser != 5:
    print(f"[1] Somar\n[2] Multiplicar\n[3] Maior Valor\n[4] Novos Números\n[5] Sair do Programa")

    escolhauser = int(input("Digite a opção: "))

    if escolhauser == 1:
        soma = valor1 + valor2
        print(f"A soma entre {valor1} e {valor2} é de: {soma}")

    elif escolhauser == 2:
        multiplicacao = valor1 * valor2
        print(f"A multiplicação entre {valor1} e {valor2} é de {multiplicacao}")

    elif escolhauser == 3:
        maior = valor1
        if valor2 > valor1:
            maior = valor2
        print(f"O maior valor é {maior}")

    elif escolhauser == 4:
        valor1 = int(input("Digite um valor: "))
        valor2 = int(input("Digite outro valor: "))

    elif escolhauser == 5:
        print("Fim do programa! Obrigado por usar! :D")
    sleep(2)
print("Terminamos por aqui!")

