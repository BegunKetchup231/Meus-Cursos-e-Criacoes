from random import choice
alu1 = str(input('Qual o nome do aluno 1? '))
alu2 = str(input('Qual o nome do aluno 2? '))
alu3 = str(input('Qual o nome do aluno 3? '))
alu4 = str(input('Qual o nome do aluno 4? '))
lista = [alu1, alu2, alu3, alu4]
sortear = choice(lista)
print(f'O nome dos alunos são {alu1}, {alu2}, {alu3} e {alu4}, e o sorteado foi o(a) {sortear}')