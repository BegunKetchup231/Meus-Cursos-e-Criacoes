largura = float(input('Qual é a altura da parede? '))
altura = float(input('Qual é a largura da parede? '))
# Área = Base x Altura
area = largura * altura
# 1 Litro de tinta pinta 2m²
quantin = area / 2
print(f'A área da parede é de {area}m² e você precisará de {quantin} Litros de tinta para pintá-la!')