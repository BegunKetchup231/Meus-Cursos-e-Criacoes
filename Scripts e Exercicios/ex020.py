from random import shuffle
alu1 = str(input('Qual o primeiro aluno? '))
alu2 = str(input('Qual o segundo aluno? '))
alu3 = str(input('Qual o terceiro aluno? '))
alu4 = str(input('Qual o quarto aluno? '))
lista = [alu1, alu2, alu3, alu4]
shuffle(lista)
print(f'A ordem de apresentação será de: ')
print(lista)