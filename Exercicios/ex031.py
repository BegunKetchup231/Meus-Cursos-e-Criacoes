# Pergunta para o usuário a distância em KM da viagem
dist = int(input('Digite a distância em KM da sua viagem: '))

# Verifica se é maior de 200km e multiplica por 0.45, se for menor de 200km multiplica por 0.50
menor = (dist * 0.50) 
maior = (dist * 0.45)

# Verifica se a distância é menor ou igual a 200km e printa a resposta
if dist <=200:
    print(f'O valor da viagem é de: R${menor:.2f}')
else:
    print(f'O valor da viagem é de: R${maior:.2f}')