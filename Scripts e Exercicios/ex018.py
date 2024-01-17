from math import radians, sin, cos, tan
ângulo = float(input('Digite um ângulo: '))
seno = sin(radians(ângulo))
cose = cos(radians(ângulo))
tang = tan(radians(ângulo))
print(f'O seno de {ângulo}° é {seno:.2f}, o cosseno é {cose:.2f} e a tangente é {tang:.2f} ')