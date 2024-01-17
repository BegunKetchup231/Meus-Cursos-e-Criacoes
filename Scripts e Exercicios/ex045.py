# Importa a biblioteca random, pra gerar números aleatórios e a time pra dar um tempo
from random import randint
from time import sleep

# Estética do minigame de jokempô.
print("-" * 40)
print((" " * 5), 'Vamos jogar jokempô?')
print('Escolha pedra, papel ou tesoura')
print('0 = Pedra')
print('1 = Papel')
print('2 = Tesoura')
print("-" * 40)

# Faz uma lista com as 3 possibilidades a cair
escolhas = ("Pedra" , "Papel" , "Tesoura")

# Randomiza a escolha da máquina
computador = randint(0 , 2)

# Escolha do usuário
usuario = int(input('Escolha: '))

# Define quem ganha ou quem perde baseado na aleatóriedade da máquina e na escolha do usuário
if usuario == 0 or usuario == 1 or usuario == 2 :
    # Apenas visual para contar o tempo do jokempo
    print("*" * 40)
    print("JO")
    sleep(1)
    print("KEM")
    sleep(1)
    print("PO!!")
    print("*" * 40)
    sleep(0.5)

# 0 Pedra, 1 Papel, 2 Tesoura.
    if computador == usuario :
        print(f'Você escolheu: {escolhas[usuario]}')
        print(f'Eu escolhi: {escolhas[computador]}')
        print(f'Nós empatamos HAHAHA!')
        print("*" * 40)
    elif computador == 1 and usuario == 0 or computador == 2 and usuario == 1 or computador == 0 and usuario == 2 :
        print(f'Você escolheu: {escolhas[usuario]}')
        print(f'Eu escolhi: {escolhas[computador]}')
        print(f'Eu ganhei!! HAHAHA, mais sorte ná próxima.')
        print("*" * 40)
    else :
        print(f'Você escolheu: {escolhas[usuario]}')
        print(f'Eu escolhi: {escolhas[computador]}')
        print(f'Você ganhou, Parabéns!!')
        print("*" * 40)
else :   
    print("*" * 40)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    print(f"O número {usuario} é não é uma opção válida")
    print("*" * 40)