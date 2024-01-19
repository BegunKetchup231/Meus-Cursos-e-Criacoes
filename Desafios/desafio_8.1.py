num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
media = (num1 + num2) / 2
print(f'A sua média final foi de {media:.1f}')
if media > 5:
    print('Você foi bem, parabéns!!')
elif media == 5:
    print('Você ficou na média ein...')
else:
    print('CHORE...')