n = str(input('Digite qualquer coisa '))
print('Você escreveu {}'.format(n))
print('Ele é alfabético?', n.isalpha())
print('Ele é um numeral?', n.isalnum())
print('Está tudo em maiúsculo?', n.isupper())
print('Ele é um decimal?', n.isdecimal())
print('Está tudo em minúsculo?', n.islower())
print('É numérico?', n.isnumeric())