# Importa a biblioteca de data da datatime
from datetime import date

# Pergunta qual ano nasceu a pessoa
ano = int(input('Qual ano você nasceu? '))

# Verifica qual o ano do computador na hora que roda o programa
anohj= date.today().year

# Verifica quantos anos tem a pessoa
idade = int(anohj) - int(ano)

# Verifica qual perfil de natação ele se encaixa usando a variável da sua 'idade' 
if idade < 9 :
    print(f'Você tem {idade} anos, e se encaixa na categoria Mirim de Natação.')
elif idade >= 9 and idade < 14 :
    print(f'Você tem {idade} anos, e se encaixa na categoria Infantil de Natação.')
elif idade >= 14 and idade < 19 :
    print(f'Você tem {idade} anos, e se encaixa na categoria Junior de Natação.')
elif idade >= 19 and idade < 25 :
    print(f'Você tem {idade} anos, e se encaixa na categoria Sênior de Natação.')
elif idade >= 25 :
    print(f'Você tem {idade} anos, e se encaixa na categoria Master de Natação.')