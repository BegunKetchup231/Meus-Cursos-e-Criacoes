# Escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros elementos de uma Seqência de Fibonacci.
# Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8

estilo = "\033[1;92m"
estilo2 = "\033[1;95m"
apagar = "\033[0m"

print("=-=" * 20)
print("Sequência de Fibonacci")
print("=-=" * 20)

numero = int(input("Quantos termos da sequência você quer? "))

termo1 = 0
termo2 = 1

print("=-=" * 20)
print(f"{estilo}{termo1} -> {termo2}{apagar}", end="")

contador = 3

while contador <= numero:
    termo3 = termo1 + termo2
    print(f"{estilo} -> {termo3}", end="")
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(f" -> {estilo2}Final da Sequência escolhida!{apagar}")