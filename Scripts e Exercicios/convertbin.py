def hexadecimal_para_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal

valores_hexadecimais = input("Cole os números hexadecimais separados por espaços (16 valores por linha):\n")
linhas = valores_hexadecimais.split("\n")

linha_atual = 0
for linha in linhas:
    valores_hexadecimais = linha.split()
    valores_decimais = []

    for i, valor_hexadecimal in enumerate(valores_hexadecimais, 1):
        valor_decimal = hexadecimal_para_decimal(valor_hexadecimal)
        valores_decimais.append(valor_decimal)

        if i % 16 == 0:
            linha_atual += 1
            print("Valores decimais correspondentes (linha", linha_atual, "):", valores_decimais)
            valores_decimais = []

    # Imprimir os valores restantes, se houver
    if valores_decimais:
        linha_atual += 1
        print("Valores decimais correspondentes (linha", linha_atual, "):", valores_decimais)
