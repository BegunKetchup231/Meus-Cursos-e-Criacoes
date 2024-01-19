# Apenas estético, mostra um "título", da calculadora de IMC
print("-" * 30)
print('Calculadora de IMC(índice de massa corporal)')
print("-" * 30)

# Pede o valor da altura do usuário e do peso
altura = float(input('Digite sua Altura: '))
peso = float(input('Digite seu Peso: ')) 

# Realiza o calculo da altura, elevando ela ao quadrado e divindo o peso pela altura
imc = peso / (altura * altura)

# Apenas para estética, multiplica o traço por 30, como se fosse uma barra!
print("-" * 30)

# Mostra na tela o valor do IMC 
print(f'Seu IMC é de {imc:.2f}')

# Compara o valor do calculo do imc, e dita em qual categoria você se encaixa
if imc < 18.5 :
    print('Você está abaixo do peso, procure um médico!')
elif imc >= 18.5 and imc < 25 :
    print('Você está no peso ideal, Parabéns!!!')
elif imc >= 25 and imc < 30 :
    print('Você está sobrepeso, cuidado!!')
elif imc >=30 and imc < 40 :
    print('Você está com obesidade, procure um médico.')
elif imc >= 40 :
    print('Você está com obesidade mórbita, procure um médico urgente!!!!')

# Apenas estética também como a parte lá de cima!
print("-" * 30)