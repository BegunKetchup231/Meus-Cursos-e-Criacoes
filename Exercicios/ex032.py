# Esta linha importa a classe date da biblioteca datetime
from datetime import date

#Esta linha solicita ao usuário que digite um ano e armazena o valor digitado na variável ano
ano = int(input('Digite um ano para verificar se ele é bissexto: '))

# Verifica se o usuário não forneceu nenhum ano como entrada, ou seja, se o valor de ano for igual a zero
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto!!')
else:
    print(f'O ano {ano} não é Bissexto :(')

"""
A expressão: (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)
verifica se o ano é divisível por 4 e não é divisível por 100, 
ou se é divisível por 400. Se o ano for divisível por 4 e não 
for divisível por 100, ou se for divisível por 400, a expressão 
retorna True e o ano é considerado bissexto. Caso contrário, a 
expressão retorna False e o ano não é considerado bissexto.
"""