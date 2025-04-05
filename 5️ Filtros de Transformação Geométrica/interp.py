from PIL import Image

# Abrir a imagem original
imagem = Image.open('5.png')

# Novo tamanho (exemplo: dobrar as dimensões)
nova_largura = imagem.width * 2
nova_altura = imagem.height * 2

# Redimensionar com interpolação BICUBIC
imagem_redimensionada = imagem.resize((nova_largura, nova_altura), Image.BICUBIC)

# Salvar a nova imagem
imagem_redimensionada.save('5mod.png')
