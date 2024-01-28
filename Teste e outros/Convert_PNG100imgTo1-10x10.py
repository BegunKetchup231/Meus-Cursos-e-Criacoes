from PIL import Image
from tkinter import Tk, filedialog
import os

def selecionar_pasta():
    root = Tk()
    root.withdraw()
    pasta_imagens = filedialog.askdirectory(title="Selecione a pasta das imagens")
    root.destroy()
    return pasta_imagens

def selecionar_destino():
    root = Tk()
    root.withdraw()
    destino = filedialog.asksaveasfilename(title="Salve a imagem resultante como", defaultextension=".png", filetypes=[("Arquivos PNG", "*.png")])
    root.destroy()
    return destino

# Selecione a pasta de imagens
pasta_imagens = selecionar_pasta()

# Tamanho de cada imagem
tamanho_imagem = (420, 420)

# Número de colunas e linhas na imagem resultante
num_colunas = 10
num_linhas = 10

# Criar uma imagem resultante com fundo transparente
imagem_resultante = Image.new('RGBA', (tamanho_imagem[0] * num_colunas, tamanho_imagem[1] * num_linhas), (0, 0, 0, 0))

# Função para extrair o número entre parênteses
def extrair_numero(nome_imagem):
    inicio = nome_imagem.find("(")
    fim = nome_imagem.find(")")
    if inicio != -1 and fim != -1:
        try:
            numero = int(nome_imagem[inicio + 1:fim])
            return numero
        except ValueError:
            pass
    return float('inf')  # Retorna infinito se não encontrar um número entre parênteses

# Iterar sobre os arquivos na pasta
nomes_imagens = os.listdir(pasta_imagens)
nomes_imagens.sort(key=extrair_numero)  # Ordenar pelo número entre parênteses
for i, nome_imagem in enumerate(nomes_imagens):
    caminho_imagem = os.path.join(pasta_imagens, nome_imagem)

    # Abrir a imagem
    try:
        imagem = Image.open(caminho_imagem).convert("RGBA")
        # Pré-multiplicar a alfa
        imagem = Image.alpha_composite(Image.new("RGBA", imagem.size, (0, 0, 0, 0)), imagem)
    except FileNotFoundError:
        print(f"Imagem {nome_imagem} não encontrada. Pulando.")
        continue

    # Calcular coordenadas para colocar a imagem
    coluna = i % num_colunas
    linha = i // num_colunas
    coordenadas = (coluna * tamanho_imagem[0], linha * tamanho_imagem[1])

    # Colocar a imagem na imagem resultante
    imagem_resultante.paste(imagem, coordenadas, imagem)

# Selecionar o destino para salvar a imagem resultante
destino = selecionar_destino()

# Salvar a imagem resultante
imagem_resultante.save(destino)

print(f"Imagem resultante salva em: {destino}")
