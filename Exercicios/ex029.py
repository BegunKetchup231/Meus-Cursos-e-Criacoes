# Solicita ao usuário qual velocidade ele estava
velo = int(input('Qual velocidade você estava? '))

# Caso ele esteja acima do limite de 80km/h pagará 7 reais por KM a mais
multa = (velo - 80) * 7

# Compara a velocidade para exibir a mensagem de multa ou parabéns
if velo <=80:
    print('Parabéns, você anda abaixo do limtie de velocidade da via!!!')
else:
    print(f'Você foi multado, e o valor da multa é de: R${multa}\nMais cuidado na próxima!!')