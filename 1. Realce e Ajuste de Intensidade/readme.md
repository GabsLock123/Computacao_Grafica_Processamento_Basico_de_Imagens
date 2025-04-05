# 💡 Aumentar Brilho de Imagem com Python

Este repositório contém um script simples em Python que utiliza a biblioteca [Pillow (PIL)](https://python-pillow.org/) para aumentar o brilho de uma imagem.

## 🖼️ Exemplo

Imagem original:

![Imagem original](1.png)

Imagem com brilho aumentado:

![Imagem com brilho aumentado](1mod.png)

## 🧠 Como funciona

O script `aumentarBrilho.py` carrega uma imagem chamada `1.png`, converte para RGB e multiplica os valores dos canais de cor (vermelho, verde e azul) de cada pixel por um fator de brilho. O valor máximo de cada canal é limitado a 255 para evitar distorções.

### Trecho principal do código:

```python
fator_brilho = 2
r = min(int(r * fator_brilho), 255)
g = min(int(g * fator_brilho), 255)
b = min(int(b * fator_brilho), 255)
pixels[x, y] = (r, g, b)
