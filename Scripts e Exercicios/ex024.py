nomeci = str(input('Digite o nome de uma cidade: ')).strip() #< Retira os espaços do inicio e final da string
verif = nomeci[:5].upper() == 'SANTO' #< Verifica nas 5 primeiras letras se tem santo jogado pra maiúsculo
print(f'A cidade {nomeci} começa com Santo? {verif}')