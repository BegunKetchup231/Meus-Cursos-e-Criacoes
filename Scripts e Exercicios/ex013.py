#Maneira 1
salario = float(input('Qual seu salário? R$'))
aumento = float(input('Quantos porcento aumentou? '))
novo = salario + (salario * aumento / 100)
print(f'Seu salário era de R${salario}, com aumento de {aumento:.0f}% passa a ser de R${novo}')
