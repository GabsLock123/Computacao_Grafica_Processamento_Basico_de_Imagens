from PIL import Image
import numpy as np
from scipy.ndimage import binary_erosion
import matplotlib.pyplot as plt

imagem = Image.open('6.png').convert('L')
matriz = np.array(imagem)

binaria = (matriz >= 128).astype(np.uint8)

estrutura = np.ones((3, 3), dtype=np.uint8)
imagem_erodida = binary_erosion(binaria, structure=estrutura).astype(np.uint8)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original binária")
plt.imshow(binaria * 255, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Após erosão")
plt.imshow(imagem_erodida * 255, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
