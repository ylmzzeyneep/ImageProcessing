import cv2
import numpy as np

# Kontrast germe fonksiyonu
def kontrast_germe(imaj, low_in, high_in, low_out, high_out):
    # Piksel değerlerini yeniden ölçeklendir
    imaj = cv2.normalize(imaj, None, alpha=low_out, beta=high_out, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    return imaj

# Görüntüyü oku
görüntü = cv2.imread('images/img.jpg')  # Görüntü dosyasının yolunu belirtin

# Girdi ve çıktı aralıklarını belirleyin
low_in = 50   # Girdi alt sınırı
high_in = 200  # Girdi üst sınırı
low_out = 0   # Çıktı alt sınırı
high_out = 255 # Çıktı üst sınırı

# Kontrast germe işlemini uygula
gerilmis_görüntü = kontrast_germe(görüntü, low_in, high_in, low_out, high_out)

# Gerilmiş görüntüyü kaydet
cv2.imwrite('kontrast_gerilmis_img.jpg', gerilmis_görüntü)

# Görüntüyü göster (isteğe bağlı)
cv2.imshow('Kontrast Gerilmiş Görüntü', gerilmis_görüntü)
cv2.waitKey(0)
cv2.destroyAllWindows()
