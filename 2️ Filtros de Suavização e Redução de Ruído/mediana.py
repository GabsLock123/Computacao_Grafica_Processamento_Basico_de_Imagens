from PIL import Image
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def filtro_mediana_numpy(imagem_pil, tamanho_janela=5):
    imagem_np = np.array(imagem_pil)
    altura, largura, canais = imagem_np.shape

    offset = tamanho_janela // 2
    imagem_expandida = np.pad(imagem_np, ((offset, offset), (offset, offset), (0, 0)), mode='edge')

    janelas = sliding_window_view(imagem_expandida, (tamanho_janela, tamanho_janela, 3))
    janelas = janelas.reshape((altura, largura, tamanho_janela * tamanho_janela, 3))

    imagem_filtrada = np.median(janelas, axis=2).astype(np.uint8)

    return Image.fromarray(imagem_filtrada)

imagem = Image.open('2.png').convert('RGB')
imagem_filtrada = filtro_mediana_numpy(imagem, tamanho_janela=5)
imagem_filtrada.save('2mods.png')
