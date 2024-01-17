km = int(input('Qual a quantidade de KM percorridos? '))
dias = int(input('Qual a quantidade de dias que você alugou?' ))
#   R$60 por dia
#   R$0,15 por km rodado
preçokm = km * 0.15
preçodias = dias * 60
print(f'Você rodou {km}km durante {dias} dias')
print(f'O total a ser pago é de R${(preçokm + preçodias):.2f}')