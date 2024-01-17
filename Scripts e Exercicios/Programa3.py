from math import sqrt

#-b +- raiz/ b²-4ac
#          2a

#----------------------------------
a = int(input("Valor do A "))
b = int(input("Valor do B "))
c = int(input("Valor do C "))
#----------------------------------
#------------Delta-----------------
# b²-4ac
delta = (b ** 2) -4 * a * c
delta2 = sqrt(delta)
baixo = 2 * a
maim = -(b)
#--------------X1------------------
x1calc = (maim + delta2) / baixo
#--------------X2------------------
x2calc = (maim - delta2) / baixo
#-------------Print ---------------
print('-' * 30)
print(f"Valor do x1 é de : {x1calc:.1f}\nValor do x2 é de : {x2calc:.1f} ")
print('-' * 30)
