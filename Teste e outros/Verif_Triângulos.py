# Entrada dos comprimentos dos lados do triângulo
a = float(input("Comprimento do lado a: "))
b = float(input("Comprimento do lado b: "))
c = float(input("Comprimento do lado c: "))

# Verificando se é um triângulo
if a + b > c and a + c > b and b + c > a:
    print("É um triângulo!")
    
    # Verificando se é retângulo
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("É um triângulo retângulo!")
    
    # Verificando se é equilátero
    elif a == b and b == c:
        print("É um triângulo equilátero!")
    
    # Verificando se é isósceles
    elif a == b or a == c or b == c:
        print("É um triângulo isósceles!")
    
    # Verificando se é escaleno
    else:
        print("É um triângulo escaleno!")
    
    # Verificando se é acutângulo ou obtusângulo
    if a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
        print("É um triângulo acutângulo!")
    else:
        print("É um triângulo obtusângulo!")
    
else:
    print("Não é um triângulo!")
