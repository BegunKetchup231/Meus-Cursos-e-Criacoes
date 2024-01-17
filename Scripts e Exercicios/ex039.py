# Importa a biblioteca de data da datatime
from datetime import date

# Pergunta qual ano nasceu a pessoa
ano = int(input('Qual ano você nasceu? '))

# Verifica qual o ano do computador na hora que roda o programa
anohj= date.today().year

# Verifica quantos anos tem a pessoa
idade = int(anohj) - int(ano)

# Se a idade for maior que 18 anos avisa que passou do tempo, e quanto tempo passou
if idade > 18 : 
    idade = idade - 18
    print(f'Você nasceu em: {ano}')
    print(f'Você já passou do tempo de alistamento a {idade} ano(s)!!')

# Se a idade for igual a 18 anos, avisa que esse é o ano!
elif idade == 18 :
    print(f'Você nasceu em: {ano}')
    print(f'Esse ano você deve se alistar amigo!! Boa sorte')

# Se não, caso seja de menor, quantos anos falta para o mesmo se alistar.
elif idade < 18 :
    idade = 18 - idade 
    print(f'Você nasceu em: {ano}')
    print(f'Faltam {idade} ano(s) para você se alistar. Prepare-se')