# Frase = 'Curso em Vídeo Python'

#Começa do 0 em diante

#           Fatiamento de String
# Frase[9]
# Pega apenas 1 letra, a 9° letra

# Frase[9:13]
# Pega do 9 até o 13 e ignora o 13, ou seja, do 9 até o 12.

# Frase[9:21]
# Pega do 9 ao 21, como o 21 não existe ele vai até o 20. 

# Frase[9:21:2]
# Começa no 9, para no 21 e pula de 2 em 2.
# Exemplo: V d o P t o

# Frase[:5]
# Começa no 0 e termina no 5, e ignora o 5.

# Frase[15:]
# Começa no 15, e vai até o final.

# Frase[9::3]
# Começa no 9, vai até o final e pula de 3 em 3.
# Exemplo: V e P h


#           Análisar uma string
#  len(frase)
# Conta quantos caracteres tem a frase, incluindo o 0

# frase.count('o')
# Conta quantos 'o' tem na frase, sem os maíusculos

# frase.count('o',0,13)
# Conta quantos 'o' tem do 0 ao 13, tirando o 13
 
# frase.find('deo')
# Mostra em qual caracter ele encontrou o 'deo' (em qual posição, no caso na "11")

# frase.find('Android')
# Irá detornar o valor -1 pois não há Android na string

# 'Curso' in frase
# Irá retornar True


#               Transformação
# frase.replace('Python','Android')
# irá trocar todas as palavras Python por Android

# frase.upper()
# O que é maiúsculo mantem, o que é minusculo transforma em maiúsculo
# Exemplo: CURSO EM VIDEO PYTHON

# frase.lower()
# O que é minúsculo mantém, e o que é maiúsculo vira minúsculo
# curso em video python

# frase.capitalize()
# Joga tudo pra minúsculo e a primeira letra fica em maiúsculo
# Exemplo: Curso em video python

# frase.title()
# Pega os espaços como quebra de palavra, e põe maiusculo em todas palavras separadas por espaço
# Exemplo: Curso Em Video Python

# frase.strip()
# Remove todos espaços inúteis no inicio e fim de uma string

# frase.rstrip()
# Remove os espaços da direita da string > 

# frase.lstrip()
# Remove os espaços da esquerda da string <

# frase.split()
# Cada palavra separada por espaço fica separada, recomeçando a contagem

#           Funcionalidade de Divisão de string

# |Curso||Em||Vídeo||Python|
#  01234  01  01234  012345
#    0     1    2       3 

# '-'.join(frase)
# Junta as palavras novamente, e coloca o - entre elas
# Exemplo: Curso-Em-Video-Python

# frase = 'Curso em Vídeo Python'
# frase = frase.replace('Python', 'Android')
# print(frase)

# frase = 'Curso em Vídeo Python'
# print(frase.upper().count('O'))
# Joga tudo pra maiúsculo e conta os "O"

# print(len(frase.strip()))
# remove os espaços da esquerda e direita e conta quantos caracteres têm