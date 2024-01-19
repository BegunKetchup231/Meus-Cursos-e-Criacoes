# Importa o módulo random para gerar números aleatórios
from random import randint
from time import sleep
# Gera um número aleatório entre 1 e 5
pensar = randint(1,5)

# Estetica do programa
print('-.-' * 20)
print('Tente adivinhar o número em que eu pensei de 0 a 5 :)')
print('-.-' * 20)

# Solicita que o usuário adivinhe qual número foi gerado e converte a resposta para inteiro
usuario = int(input('Chute qual número eu pensei de 0 a 5: '))

# Simula que o PC está comparando as respostas
print('Comparando as respostas...')
sleep(3)

# Compara a resposta do usuário com o número gerado e exibe uma mensagem de acerto ou erro
print('-' * 40)
if usuario == pensar:
    print('Parabéns você acertou!!!')
else:
    print('Como diz o faustão... EERRRROUUU')
print('-' * 40)