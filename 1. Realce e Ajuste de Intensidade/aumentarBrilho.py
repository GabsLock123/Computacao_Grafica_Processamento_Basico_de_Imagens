from PIL import Image


imagem = Image.open('1.png')
imagem = imagem.convert('RGB')  


fator_brilho = 2

pixels = imagem.load()
largura, altura = imagem.size

for x in range(largura):
    for y in range(altura):
        r, g, b = pixels[x, y]
        r = min(int(r * fator_brilho), 255)
        g = min(int(g * fator_brilho), 255)
        b = min(int(b * fator_brilho), 255)
        pixels[x, y] = (r, g, b)

imagem.save('1mod.png')
