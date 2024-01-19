nome = str(input('Digite seu nome: ')).strip()
fat = nome.upper().split()
verif = 'SILVA' in (fat[:])
print(f'O seu nome tem a palavra silva? {verif}')