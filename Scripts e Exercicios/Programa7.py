from math import sqrt

# -b +- / b²-4ac    
#      2a 
print("=-" * 20)
print((" " * 8), 'Calculadora de Bháskara')
print("=-" * 20)
#--------------------------
a = int(input('Digite o valor do A: '))
b = int(input('Digite o valor do B: '))
c = int(input('Digite o valor do C: '))
#---------------------------
delta = (b ** 2) -4 * a * c
#---------------------------
baixo = 2 * a
#---------------------------
raiz = sqrt(delta)
#---------------------------

x1 = (-b + raiz) / baixo
x2 = (-b - raiz) / baixo

print('O valor do A é {}, o valor do B é {} e o valor do C é {}'.format(a, b, c))
print('E o x1 equivale a {:.2f}, e o x2 equivale a {:.2f}'.format(x1, x2))

