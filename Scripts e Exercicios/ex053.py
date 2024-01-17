# Desenvolva um programa que leia uma frase e diga se ela é um palíndromo, ou seja, pode ser lida 
# de trás pra frente e de frente pra trás


cor_verde = '\033[92m'
reset = '\033[0m'

frase = str(input('Digite uma frase: ')).lower().strip()

frase_invertida = frase[::-1]

frase_invertida = (''.join(frase_invertida))

if frase_invertida == frase :

    print('A frase: ', cor_verde+f'{frase}' ,reset ,'é um palíndromo')
    
else : 
    
    print('A frase: ', cor_verde+f'{frase}', reset ,'não é um palíndromo')