# Desenvolva um programa que leia uma frase e diga se ela é um palíndromo, ou seja, pode ser lida 
# de trás pra frente e de frente pra trás

print("Verificando se é um Palíndromo")

frase = str(input("Digite uma frase: ")).strip().upper()

# Removendo espaço entre as palavras:
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if str(inverso) == frase:
    print(f"A frase: {frase} é um palíndromo!!")
else:
    print(f"A frase: {frase} não é um palíndromo")