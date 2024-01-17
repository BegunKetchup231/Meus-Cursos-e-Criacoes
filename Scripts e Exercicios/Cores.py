#       Cores no terminal

#       Estilo \ Stile
#   0 = none
#   1 = negrito
#   4 = sublinhado
#   7 = negativo


#       Texto \ Text
#   30 = Branco
#   31 = Vermelho
#   32 = Verde
#   33 = Amarelo
#   34 = Azul
#   35 = Roxo
#   36 = Ciano
#   37 = Cinza (padrão)


#       Fundo \ Back
#   40 = Branco
#   41 = Vermelho
#   42 = Verde
#   43 = Amarelo
#   44 = Azul
#   45 = Roxo
#   46 = Ciano
#   47 = Cinza (padrão)

#       Comando para resetar a cor
#   \033[0m

#       Exemplo
print('\033[1;33;44mOlá mundo\033[0m')


print('{}Olá, Mundo{}'.format('\033[1;33;44m', '\033[0m'))