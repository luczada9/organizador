import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

def organizar_arquivos(pasta):
    if not os.path.exists(pasta):
        return "Pasta não encontrada."

    arquivos = os.listdir(pasta)
    if not arquivos:
        return "Nenhum arquivo encontrado."

    # Dicionário com categorias e extensões
    categorias = {
        'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.odt'],
        'Planilhas': ['.xls', '.xlsx', '.csv', '.ods'],
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
        'Músicas': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
        'Vídeos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'],
        'Compactados': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Executáveis': ['.exe', '.msi', '.bat'],
        'Códigos': ['.py', '.ipynb', '.js', '.html', '.css', '.cpp', '.java'],
        'Outros': []  # Para arquivos sem categoria
    }

    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_completo):
            extensao = os.path.splitext(arquivo)[-1].lower()
            categoria_encontrada = 'Outros'

            # Verifica a categoria do arquivo
            for categoria, extensoes in categorias.items():
                if extensao in extensoes:
                    categoria_encontrada = categoria
                    break

            # Cria a pasta da categoria, se não existir
            pasta_categoria = os.path.join(pasta, categoria_encontrada)
            if not os.path.exists(pasta_categoria):
                os.makedirs(pasta_categoria)

            # Move o arquivo para a pasta da categoria
            shutil.move(caminho_completo, os.path.join(pasta_categoria, arquivo))

    return f"{len(arquivos)} arquivo(s) organizados em categorias com sucesso."

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Arquivos")
        self.root.geometry("500x250")

        self.pasta = tk.StringVar()

        tk.Label(root, text="Pasta a organizar:").pack(pady=5)
        tk.Entry(root, textvariable=self.pasta, width=60).pack()
        tk.Button(root, text="Selecionar Pasta", command=self.selecionar_pasta).pack(pady=5)

        tk.Button(root, text="Organizar agora", command=self.organizar).pack(pady=10)

        self.resultado = tk.Text(root, height=6, width=60)
        self.resultado.pack(pady=10)

    def selecionar_pasta(self):
        pasta_escolhida = filedialog.askdirectory()
        if pasta_escolhida:
            self.pasta.set(pasta_escolhida)

    def organizar(self):
        caminho = self.pasta.get()
        msg = organizar_arquivos(caminho)
        self.resultado.insert(tk.END, msg + "\n")
        self.resultado.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
