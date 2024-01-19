#          Matematicamente:
num = int(input('Digite um número de 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'O número {num} tem: ')
print(f'Unidades: {unidade}')
print(f'Dezenas:  {dezena}')
print(f'Centena:  {centena}')
print(f'Milhar:   {milhar}')