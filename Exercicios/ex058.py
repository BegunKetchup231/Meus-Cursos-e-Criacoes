# Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

pensamento = randint(1, 10)

print(f"\033[1;93mEu irei pensar em um número de 1 a 10... Tente adivinhar...\033[0m")

numero = int(input("Digite: "))

while numero != pensamento:
    print("Você errou... Tente novamente! ")
    numero = int(input("Digite: "))

print(f"Eu pensei no número {pensamento} e você no {numero}, você acertou, genial!!")