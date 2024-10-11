import cv2
import numpy as np

# Gama dönüşüm fonksiyonu
def gama_donusu(imaj, gama):
    # Gama değeri ile normalize et
    imaj = imaj / 255.0
    imaj_gama = np.power(imaj, gama)
    imaj_gama = (imaj_gama * 255).astype(np.uint8)
    return imaj_gama

# Görüntüyü oku
görüntü = cv2.imread('images/img.jpg')  # Görüntü dosyasının yolunu belirtin

# Gama değerini belirleyin (örneğin, 2.2)
gama_degeri = 2.2

# Gama dönüşümünü uygula
gama_görüntü = gama_donusu(görüntü, gama_degeri)

# Gama dönüştürülmüş görüntüyü kaydet
cv2.imwrite('gama_donusu_img.jpg', gama_görüntü)

# Görüntüyü göster (isteğe bağlı)
cv2.imshow('Gama Dönüşümü Uygulandı', gama_görüntü)
cv2.waitKey(0)
cv2.destroyAllWindows()
