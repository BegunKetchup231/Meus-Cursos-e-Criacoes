# Pede para o usuário digitar 3 valores de retas de um triângulo ou não.
reta1 = float(input('Digite o valor da reta 1: '))
reta2 = float(input('Digite o valor da reta 2: '))
reta3 = float(input('Digite o valor da reta 3: '))

# Verifica inicialmente se as 3 retas formam um triângulo.
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2 :
    print(f'Essas 3 retas {reta1:.2f}, {reta2:.2f} e {reta3:.2f} formam um triângulo')

# Se as 3 retas forem de valores iguais ele é um triângulo Equilátero.
    if reta1 == reta2 and reta1 == reta3 :
        print('E esse triângulo é um triângulo Equilátero!!')

# Se apenas 2 lados forem iguais e um diferente ele é um triângulo Isóceles.
    elif reta1 == reta2 and reta1 != reta3 or reta1 == reta3 and reta1 != reta2 or reta2 == reta3 and reta2 != reta1 :
        print('E esse triângulo é um triângulo Isóceles')

# Se os 3 lados forem de valores diferentes e formarem triângulo ele é um triângulo Escaleno.
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3 :
        print('E esse triângulo é um triângulo Escaleno')

# Se a comprovação de que não é triângulo for correta, apenas pula o passo acima e identifica que não são triângulos.
else :
    print(f'Essas 3 retas NÃO formam um triângulo!')