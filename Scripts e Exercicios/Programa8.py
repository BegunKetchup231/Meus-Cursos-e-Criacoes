print("-" * 19)
print((" " * 4), "Bot number")
print("-" * 19)
quant = int(input('Quantos números são? (de 1 a 10) '))
print("-" * 19)

ordens = []
numeros = []


if quant >= 1 and quant <= 10:
    for quantidade in range(quant):
        
        ordem = int(input('Cliente Ordem: '))
        num = int(input('Número: '))
        ordens.append(ordem)
        numeros.append(num)

    for i in range(quant):
    
        print("-" * 40)
        print(f'Cliente: {ordens[i]} = Número: {numeros[i]}')
        print(f'Link rápido: https://wa.me/55{numeros[i]}')
        print("-" * 40)
        
else:
    print('Escolha uma opção válida!!!')
