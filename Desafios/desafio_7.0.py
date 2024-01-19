frase = 'Curso em Vídeo Python'
print(frase[0:])
print(frase.upper().count('O')) #<Joga tudo pra maiusculo e conta os O
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)

# Irá printar só o primeiro da lista (Curso)
frase = 'Curso em video'
dividido = frase.split()
print(dividido[0])
print(dividido[2][3]) #< Pega a 2 palavra, e a 3 letra
#-------------------------

print("""
Prints the values to a stream, or to sys.stdout by default.
sep
  string inserted between values, default a space.
end
  string appended after the last value, default a newline.
file
  a file-like object (stream); defaults to the current sys.stdout.
flush""")