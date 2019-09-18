from PIL import Image
from random import randint
img = Image.new('RGB', (400, 300))
pixels = img.load()
for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixels[x, y] = (randint(0, 255), randint(0, 255),  randint(0, 255))
img.show()
