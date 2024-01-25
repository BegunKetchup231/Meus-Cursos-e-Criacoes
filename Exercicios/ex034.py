# Pergunta qual o salário do funcionário
sala = float(input('Qual o salário do funcionário? R$'))

# Verifica o aumento na % do salário se for maior que 1250 ou menor
superior = sala + (sala * 10 / 100)
inferior = sala + (sala * 15 / 100)

# Se for maior ou igual a 1250 aumenta 10% no salário, se não aumenta 15% do salário
if sala >= 1250.00:
    print(f'O seu novo salário é de R${superior:.2f}')
else:
    print(f'O seu novo salário é de R${inferior:.2f}')
    