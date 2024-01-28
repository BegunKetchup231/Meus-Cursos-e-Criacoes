from PIL import Image, ImageTk
from tkinter import Tk, filedialog, Label, Button, Canvas, Frame, TOP, BOTH, X
import os 

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Combinação de Ícones")
        self.pasta_imagens = ""
        self.destino = ""
        self.tamanho_imagem = (420, 420)
        self.num_colunas = 10
        self.num_linhas = 10
        self.criar_widgets()

    def criar_widgets(self):
        frame_pasta = Frame(self.root)
        frame_pasta.pack(fill=X)

        Label(frame_pasta, text="Selecione a pasta das imagens:").pack(side="left", padx=5)
        Button(frame_pasta, text="Escolher Pasta", command=self.selecionar_pasta).pack(side="left", padx=5)

        frame_destino = Frame(self.root)
        frame_destino.pack(fill=X)

        Label(frame_destino, text="Selecione onde salvar a imagem resultante:").pack(side="left", padx=5)
        Button(frame_destino, text="Escolher Destino", command=self.selecionar_destino).pack(side="left", padx=5)

        Button(self.root, text="Combinação de Ícones", command=self.combinar_icones).pack(pady=10)

        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=True)

    def selecionar_pasta(self):
        self.pasta_imagens = filedialog.askdirectory(title="Selecione a pasta das imagens")
        print(f"Pasta selecionada: {self.pasta_imagens}")

    def selecionar_destino(self):
        self.destino = filedialog.asksaveasfilename(title="Salve a imagem resultante como", defaultextension=".png", filetypes=[("Arquivos PNG", "*.png")])
        print(f"Destino selecionado: {self.destino}")

    def combinar_icones(self):
        if not self.pasta_imagens or not self.destino:
            print("Por favor, selecione a pasta das imagens e o destino.")
            return

        imagem_resultante = Image.new('RGBA', (self.tamanho_imagem[0] * self.num_colunas, self.tamanho_imagem[1] * self.num_linhas), (0, 0, 0, 0))

        nomes_imagens = os.listdir(self.pasta_imagens)
        nomes_imagens.sort(key=self.extrair_numero)

        for i, nome_imagem in enumerate(nomes_imagens):
            caminho_imagem = os.path.join(self.pasta_imagens, nome_imagem)

            try:
                imagem = Image.open(caminho_imagem).convert("RGBA")
                imagem = Image.alpha_composite(Image.new("RGBA", imagem.size, (0, 0, 0, 0)), imagem)
            except FileNotFoundError:
                print(f"Imagem {nome_imagem} não encontrada. Pulando.")
                continue

            coluna = i % self.num_colunas
            linha = i // self.num_colunas
            coordenadas = (coluna * self.tamanho_imagem[0], linha * self.tamanho_imagem[1])

            imagem_resultante.paste(imagem, coordenadas, imagem)

        imagem_resultante.save(self.destino)
        print(f"Imagem resultante salva em: {self.destino}")

        # Exibir a imagem resultante na interface gráfica
        imagem_exibicao = ImageTk.PhotoImage(imagem_resultante)
        self.canvas.config(width=imagem_resultante.width, height=imagem_resultante.height)
        self.canvas.create_image(0, 0, anchor="nw", image=imagem_exibicao)
        self.root.update_idletasks()  # Atualizar a interface gráfica

    def extrair_numero(self, nome_imagem):
        inicio = nome_imagem.find("(")
        fim = nome_imagem.find(")")
        if inicio != -1 and fim != -1:
            try:
                numero = int(nome_imagem[inicio + 1:fim])
                return numero
            except ValueError:
                pass
        return float('inf')

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.geometry("800x600")
    root.mainloop()
