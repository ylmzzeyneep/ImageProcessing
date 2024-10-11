import cv2
import numpy as np

# Görüntüyü oku
görüntü = cv2.imread('images/img.jpg')  # Görüntü dosyasının yolunu belirtin

# Görüntüyü diziye çevir
pikseller = np.array(görüntü)

# Negatifini al
negatif = 255 - pikseller

# Negatif görüntüyü kaydet
cv2.imwrite('negatif_img.jpg', negatif)

# Görüntüyü göster (isteğe bağlı)
cv2.imshow('Negatif Görüntü', negatif)
cv2.waitKey(0)
cv2.destroyAllWindows()
