def hexadecimal_para_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal

def converter_arquivo_hexadecimal(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r') as arquivo_hex:
        with open(arquivo_saida, 'w') as arquivo_dec:
            for linha in arquivo_hex:
                linha = linha.strip()  # Remove espaços e quebras de linha
                valor_decimal = hexadecimal_para_decimal(linha)
                arquivo_dec.write(str(valor_decimal) + '\n')

# Exemplo de uso:
converter_arquivo_hexadecimal('Title.hex', 'Title.txt')
