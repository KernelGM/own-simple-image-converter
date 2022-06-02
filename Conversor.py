from PIL import Image
import os

lista = os.listdir()

for i in lista:
    if i.endswith('.jpg'):
        imagem = Image.open(f'{i}')
        imagem.save(
            f"jpg/{i.replace('.jpg', '.png')}")
