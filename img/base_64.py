## pip install pybase64
import PIL.Image as Image

import base64
from io import BytesIO


# Abre o arquivo de imagem
with open("C:\\pydev\\img.blob\\bb.jpg", "rb") as image_file:
    # criptografa o arquivo em base 64
    data = base64.b64encode(image_file.read())

#print(data)

# desciptografa o arquivo em base 64
im = Image.open(BytesIO(base64.b64decode(data)))
im.save('C:\\pydev\\img.blob\\image1.png', 'PNG')

# visualiza o arquivo
im.show()
