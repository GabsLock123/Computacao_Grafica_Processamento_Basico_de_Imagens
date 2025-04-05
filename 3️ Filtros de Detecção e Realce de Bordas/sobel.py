from PIL import Image
import numpy as np

def aplicar_filtro_sobel(imagem):
    imagem = imagem.convert('L')
    matriz = np.array(imagem, dtype='int32')

    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])

    altura, largura = matriz.shape
    resultado = np.zeros((altura, largura), dtype='uint8')

    for i in range(1, altura-1):
        for j in range(1, largura-1):
            regiao = matriz[i-1:i+2, j-1:j+2]
            gx = np.sum(sobel_x * regiao)
            gy = np.sum(sobel_y * regiao)
            gradiente = np.sqrt(gx**2 + gy**2)
            resultado[i, j] = min(255, int(gradiente))

    return Image.fromarray(resultado)

imagem_original = Image.open('3.png')
imagem_sobel = aplicar_filtro_sobel(imagem_original)

imagem_sobel.save('3mod.png')
