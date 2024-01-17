# Pede ao usuário para digitar 2 notas
nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite outra agora: '))

# Calcula a média das duas notas
media = float((nota1 + nota2) / 2)

# Se a média for menor que 5, retorna que ele foi reprovado.
if media < 5.0 :
    print('Você foi reprovado, estude mais...')

# Se a média for maior ou igual a 5 e menor ou igual a 6.9 você fica de recuperação
elif media >= 5.0 and media <= 6.9 :
    print('Você ficou de recuperação, foco!')

# Se não é nenhuma das duas acima você é aprovado!
else :
    print('Você foi aprovado, Parabéns!!')
    