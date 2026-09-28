# organizador-de-pastas
# 📂 Organizador de Arquivos em Python

Um organizador automático de arquivos desenvolvido em Python para facilitar a organização de pastas com muitos arquivos.

## 💡 Sobre o projeto

Quando uma pasta começa a acumular muitos arquivos, como imagens, vídeos, áudios, documentos e arquivos compactados, encontrar um arquivo específico pode se tornar difícil.

Este projeto automatiza parte desse processo.

O programa analisa os arquivos de uma pasta, identifica o tipo de cada arquivo pela sua extensão e o move automaticamente para uma pasta correspondente.

### Exemplo

Antes:

```text
📁 pasta de arquivos 1
├── foto.jpg
├── video.mp4
├── musica.mp3
├── trabalho.pdf
├── arquivo.zip
└── imagem.png

depois:
📁  pasta de aquivos 1
├── 📁 Imagens
│   ├── foto.jpg
│   └── imagem.png
│
├── 📁 Vídeos
│   └── video.mp4
│
├── 📁 Áudios
│   └── musica.mp3
│
├── 📁 Documentos
│   └── trabalho.pdf
│
└── 📁 Compactados
    └── arquivo.zip
