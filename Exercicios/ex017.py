#        | Teorema de pitágoras |
from math import sqrt
cat1 = int(input('Digite o cateto oposto '))
cat2 = int(input('Digite o cateto adjacente '))
hipot = sqrt((cat1 ** 2) + (cat2 ** 2))
print(f'O valor da hipotenusa é de {hipot:.2f}')