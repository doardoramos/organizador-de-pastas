#organizador de projeto

import os
import shutil

# Pede o caminho da pasta que queres organizar no teu PC
caminho = input("Digita ou cola o caminho da pasta (ex: C:\\Users\\seu_usuario\\Downloads): ")

# Verifica se o caminho digitado existe antes de continuar
if not os.path.exists(caminho):
    print("O caminho especificado não existe! Verifica e tenta novamente.")
    exit()

# caminho das pastas
pasta_imagens = os.path.join(caminho, "Imagens")
pasta_videos = os.path.join(caminho, "Vídeos")
pasta_audios = os.path.join(caminho, "Áudios")
pasta_documentos = os.path.join(caminho, "Documento")
pasta_compactados = os.path.join(caminho, "Arquivo compactado")
pasta_outros = os.path.join(caminho, "Outros")

os.makedirs(pasta_imagens, exist_ok=True)
os.makedirs(pasta_videos, exist_ok=True)
os.makedirs(pasta_audios, exist_ok=True)
os.makedirs(pasta_documentos, exist_ok=True)
os.makedirs(pasta_compactados, exist_ok=True)
os.makedirs(pasta_outros, exist_ok=True)

arquivos = os.listdir(caminho)

for file in arquivos:
    nome = file.lower()
    caminho_arquivo = os.path.join(caminho, file)
    if os.path.isfile(caminho_arquivo):
        print(file)

        if nome.endswith((".jpg", ".jpeg", ".png", ".gif")):
            print(file, "-> Imagem")
            shutil.move(caminho_arquivo, os.path.join(pasta_imagens, file))

        elif nome.endswith((".mp4", ".mov", ".avi", ".mkv")):
            print(file, "-> Vídeo")
            shutil.move(caminho_arquivo, os.path.join(pasta_videos, file))

        elif nome.endswith((".mp3", ".wav", ".flac")):
            print(file, "-> Áudio")
            shutil.move(caminho_arquivo, os.path.join(pasta_audios, file))

        elif nome.endswith((".pdf", ".docx", ".txt")):
            print(file, "-> Documento")
            shutil.move(caminho_arquivo, os.path.join(pasta_documentos, file))

        elif nome.endswith((".zip", ".rar", ".7z")):
            print(file, "-> Arquivo compactado")
            shutil.move(caminho_arquivo, os.path.join(pasta_compactados, file))

        else:
            print(file, "-> Tipo de arquivo desconhecido")
            shutil.move(caminho_arquivo, os.path.join(pasta_outros, file))











		
