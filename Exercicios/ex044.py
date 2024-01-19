# Pede au usário o valor do produto
valorprod = float(input('Digite o Valor do Produto: '))

# Pede qual a forma de pagamento
print("-" * 40)
print('Qual a forma de pagamento?')
print('1 - Á vista (Dinheiro/Cheque)')
print('2 - Á vista (Cartão 1x)')
print('3 - Duas vezes no Cartão')
print('4 - Três vezes ou mais no Cartão ')
print("-" * 40)

# Dá ao usuário a escolha do número correspondente a opção desejada
escolha = int(input('Escolha o número correspondente: '))

# Á vista - Dinheiro/Cheque
avista = valorprod - (valorprod * (10 / 100))

# Á vista - Cartão
avistac = valorprod - (valorprod * (5 / 100))

# Até 2x no cartão
card2x = valorprod

# Cartão 3x ou mais
card3xmais = valorprod + (valorprod * (20 / 100))

# Define o valor do produto baseado na "escolha" do usuário
if escolha == 1 :
    print(f'O valor total do produto á vista fica em: R${avista:.2f}')
elif escolha == 2 :
    print(f'O valor total do produto no cartão fica em: R${avistac:.2f}')
elif escolha == 3 :
    print(f'O valor total do produto em 1 ou 2x fica em: R${card2x:.2f}')
elif escolha == 4 :
    print(f'O valor do produto em 3x ou mais fica em: R${card3xmais:.2f}')