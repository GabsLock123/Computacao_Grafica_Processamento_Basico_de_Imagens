from PIL import Image

imagem = Image.open('5.png')

nova_largura = imagem.width * 2
nova_altura = imagem.height * 2

imagem_redimensionada = imagem.resize((nova_largura, nova_altura), Image.BICUBIC)

imagem_redimensionada.save('5mod.png')
