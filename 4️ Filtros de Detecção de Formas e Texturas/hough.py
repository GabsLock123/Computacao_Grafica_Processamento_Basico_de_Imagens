from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import feature, transform, color
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.draw import circle_perimeter

imagem = Image.open('4.png').convert('L')
matriz = np.array(imagem)

bordas = feature.canny(matriz, sigma=2.0)

h, theta, d = transform.hough_line(bordas)
picos_linhas = transform.hough_line_peaks(h, theta, d)

radii = np.arange(15, 40, 1)  
hough_res = hough_circle(bordas, radii)
acumulador, cx, cy, raios_detectados = hough_circle_peaks(hough_res, radii, total_num_peaks=5)

imagem_colorida = color.gray2rgb(matriz)

for _, angle, dist in zip(*picos_linhas):
    y0 = dist / np.sin(angle)
    y1 = (dist - matriz.shape[1] * np.cos(angle)) / np.sin(angle)
    ax_y = [y0, y1]
    ax_x = [0, matriz.shape[1]]
    plt.plot(ax_x, ax_y, '-r')

for center_y, center_x, raio in zip(cy, cx, raios_detectados):
    rr, cc = circle_perimeter(center_y, center_x, raio)
    rr = np.clip(rr, 0, matriz.shape[0] - 1)
    cc = np.clip(cc, 0, matriz.shape[1] - 1)
    imagem_colorida[rr, cc] = (0, 0, 255)

fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(imagem_colorida)
for _, angle, dist in zip(*picos_linhas):
    y0 = dist / np.sin(angle)
    y1 = (dist - matriz.shape[1] * np.cos(angle)) / np.sin(angle)
    ax.plot((0, matriz.shape[1]), (y0, y1), '-r')  

ax.set_title('Linhas (vermelho) e Círculos (azul) detectados')
ax.axis('off')
plt.tight_layout()
plt.show()
