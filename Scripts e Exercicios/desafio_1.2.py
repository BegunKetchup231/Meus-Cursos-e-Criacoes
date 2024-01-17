#Opção 1 (errada)
número1 = input('Escolha um número')
número2 = input('Agora escolha outro')
print(número1 + número2)

#Opção 2 (errada, soma)
número1 = input('Digite um número')
número2 = input('Agora outro')
soma = número1 + número2
print('A soma vale',soma)

#Opção 3 (certa)
número1 = int(input('Digite um número'))
número2 = int(input('Agora outro'))
soma = número1 + número2
print('A soma vale',soma)

#Outro exemplo:
print('A soma vale {}'.format(soma))