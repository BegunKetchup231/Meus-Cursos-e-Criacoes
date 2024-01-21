# Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0, com 
# uma pausa de 1 segundo entre eles.

from time import sleep

Estilo = "\033[1m"
Cor = "\033[91m"
Cor2 = "\033[93m"

print(Estilo + Cor2 + "Contagem para os fogos...")

for contagem in range(10, -1, -1):
    sleep(1)
    print(contagem)
print(Estilo + Cor + "Kabum, Kabum... Feliz Ano Novo!!!")