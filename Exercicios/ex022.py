nome = str(input('Qual o seu nome completo? ')).strip()
print(f'Seu nome com todas as letras maíusculas: {(nome.upper())}')
print(f'Seu nome com todas as letras minúsculas: {(nome.lower())}')
contna = len(nome) - nome.count(' ')#<<<<<<< len do nome menos a quantidade de espaços.
print(f'Quantidades de letras que tem seu nome: {contna} ')
split = nome.split()
print(f'O seu primeiro nome tem {len(split[0])} letras')
                                    #^^^^ Conta a quantidade de letras na palavra 0 splitada.