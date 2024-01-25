# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o valor 999 digitado no console

# Estilo de cores e estilo limpo
color = "\033[1;92m"
color2 = "\033[1;95m"
stop = "\033[0m"

# Valores iniciais
contador = digitado = soma = 0

# Estética inicial
print(f"{color2}-=-" * 30)
print(f"{" " * 15}Digite números de sua escolha para no final somá-los")
print(f"{color2}-=-{stop}" * 30)

# Loop 
while digitado != 999:
    digitado = int(input("Digite o número, ou [999] para parar: "))
    contador += 1
    soma += digitado
    
# Estética final
print(f"{color}-=-{stop}" * 30)
print(f"Programa Finalizado com Sucesso!!")
print(f"A soma de todos os números é de: {color}{soma - 999}{stop} desconsiderando o valor 999")
print(f"A quantidade de números digitados foi de: {color}{contador - 1}{stop}")
print(f"{color}-=-{stop}" * 30)
