import cv2
import numpy as np

# Görüntüyü oku
görüntü = cv2.imread('images/img.jpg')  # Görüntü dosyasının yolunu belirtin

if görüntü is None:
    print("Görüntü dosyası bulunamadı. Lütfen yolu kontrol edin.")
else:
    # Görüntüyü logaritmik dönüşüme tabi tut
    # Görüntü değerlerini float32 formatına dönüştür
    görüntü_float = np.float32(görüntü) + 1  # Logaritma negatif değer vermemesi için +1 ekleyin
    logaritmik_görüntü = np.log(görüntü_float)

    # Normalize et
    normalized_görüntü = cv2.normalize(logaritmik_görüntü, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # 8-bit unsigned integer'a dönüştür
    logaritmik_görüntü = normalized_görüntü.astype(np.uint8)

    # Görüntüyü kaydet
    cv2.imwrite('logaritmik_img.jpg', logaritmik_görüntü)

    # Görüntüyü göster (isteğe bağlı)
    cv2.imshow('Logaritmik Görüntü', logaritmik_görüntü)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
