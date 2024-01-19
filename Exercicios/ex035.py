# Pede para o usuário 3 valores de retas
reta1 = float(input('Digite uma das retas: '))
reta2 = float(input('Digite a segunda reta: '))
reta3 = float(input('Digite a terceira reta: '))

# Verifica se a soma da primeira reta + a segunda reta é maior que a terceira reta!
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As retas formam um triângulo sim!!')
else:
    print('As retas não formam um triângulo :(')