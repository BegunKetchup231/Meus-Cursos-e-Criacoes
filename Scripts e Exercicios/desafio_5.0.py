#Pra quebrar a linha usa \n

n1 = float(input('Escolha um valor '))
n2 = float(input('Agora outro valor '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
divint= n1 // n2
pot = n1 ** n2 
res = n1 % n2
quan1 = n1 ** (1/2)
quan2 = n2 ** (1/2) #Se for elevar ao cubo usa (número ** (1/3))

print(f'A soma de {n1} e {n2} é {s}, a subtração é {su}, a multiplicação é {m}', end=' ') #< pra não quebrar a linha usa end=''
print(f'A soma de {n1} e {n2} é {s}, a subtração é {su}, a multiplicação é {m}')
print(f'A divisão é {d:.2f}, a divisão inteira é {divint}, a potenciação é {pot} e o resto é {res}')
print(f'A raíz quadrada de {n1} é {quan1:.2f} e de {n2} é {quan2:.2f}') #Com 2 números depois da vírgula
print(f'A raíz quadrada de {n1} é {int(quan1)} e de {n2} é {int(quan2)}') #Convertido pra número inteiro
print(f'soma {n1+n2:.0f}') #Sem precisar atribuir uma variável para cada situação