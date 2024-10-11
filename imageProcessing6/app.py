import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle (gri tonlama)
image = cv2.imread('images/img.jpg', cv2.IMREAD_GRAYSCALE)


# Kontrast germe (kontrast iyileştirme) fonksiyonu
def contrast_stretching(image):
    # Görüntüdeki minimum ve maksimum piksel değerlerini bul
    min_val = np.min(image)
    max_val = np.max(image)

    # Kontrast germe işlemi: piksel değerlerini yeniden ölçeklendir
    stretched = (image - min_val) * (255 / (max_val - min_val))
    return np.uint8(stretched)


# Kontrast gerilmiş görüntüyü elde et
stretched_image = contrast_stretching(image)

# Histogram eşitleme işlemi
equalized_image = cv2.equalizeHist(image)

# Orijinal, gerilmiş ve eşitlenmiş görüntüleri göster
plt.figure(figsize=(18, 6))

# 1. Orijinal Görüntü
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

# 2. Kontrast Gerilmiş Görüntü
plt.subplot(1, 3, 2)
plt.imshow(stretched_image, cmap='gray')
plt.title('Kontrast Gerilmiş Görüntü')
plt.axis('off')

# 3. Eşitlenmiş Görüntü
plt.subplot(1, 3, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Eşitlenmiş Görüntü')
plt.axis('off')

# Görüntüleri göster
plt.show()
