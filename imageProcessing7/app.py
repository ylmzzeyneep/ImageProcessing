import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü gri ölçekli yükle
image = cv2.imread('images/img.jpg', 0)

# Boş bir liste bit düzeylerini depolamak için
bit_planes = []

# Görüntüyü 8 bit düzeyine ayır
for i in range(8):
    # Görüntüdeki her pikselin i'inci bitini almak için bitwise işlemi
    bit_plane = cv2.bitwise_and(image, 2**i)
    # Elde edilen bit düzeyini tam olarak siyah-beyaz aralığına taşı
    bit_plane = bit_plane * 255 // (2**i)
    bit_planes.append(bit_plane)

# Görselleri gösterme
plt.figure(figsize=(10, 6))
for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(bit_planes[i], cmap='gray')
    plt.title(f'Bit Plane {i+1}')
    plt.xticks([]), plt.yticks([])

plt.show()
