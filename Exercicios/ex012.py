preprod = float(input('Qual o preço do produto? '))
desconto = float(input('Qual o desconto? '))
valorfinal = preprod - (preprod * desconto / 100)
print(f'O produto antes custava {preprod:.2f} agora custa {valorfinal:.2f} com {desconto}% de desconto')

