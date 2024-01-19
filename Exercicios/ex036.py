# Pede o valor da casa, do salário e quantos anos quer pagá-la
valorc = float(input('Qual o valor da casa? '))
sala = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos você quer pagar? '))

# Checa o valor da parcela e quanto é 30% do salário da pessoa.
parce = valorc / (anos * 12)
trint = sala * (30 / 100)

# Se o valor da parcela for maior que 30% do salário ela não é aprovada!
if int(parce) >= int(trint) :
    print(f'O valor da casa é R${valorc:.2f}; ')
    print(f'Em {anos} anos, daria {parce:.2f} por mês! ')
    print(f'Isso excede (30%) do seu salário mensal ')
    print(f'Por isso seu empréstimo foi NEGADO. Desculpe.')
    
# Se for menor que 30% ela é aprovada!
else :
    print(f'O valor da casa é R${valorc:.2f}; ')
    print(f'Em {anos} anos, daria {parce:.2f} por mês! ')
    print(f'Isso não excede (30%) do seu salário mensal ')
    print(f'Então seu empréstimo foi APROVADO!! Parabéns.')