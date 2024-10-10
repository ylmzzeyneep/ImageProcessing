import cv2
import numpy as np
import matplotlib.pyplot as plt

# Resmi yükle
image_path = 'images/img.png'
image = cv2.imread(image_path)

# Görüntüyü BGR'den RGB'ye çevir
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Gri tonlamaya çevir ve beyaz pikselleri bul
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Beyaz pikseller için eşik belirleme
_, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Kırmızı çizginin y ekseni koordinatı
line_y = 50

# En fazla beyaz pikseli olan şişeyi belirlemek için değişkenler
max_white_pixels = 0
best_bottle_x = 0
best_bottle_w = 0

# Şişelerin genişliği ve yerleşim düzeni hakkında varsayımlar
bottle_width = image_rgb.shape[1] // 5  # 5 şişe varsayıyoruz
for i in range(5):  # 5 şişe kontrol ediyoruz
    # Her bir şişenin altındaki alanı kes
    x_start = i * bottle_width
    x_end = (i + 1) * bottle_width
    bottle_area = threshold[line_y:, x_start:x_end]

    # Beyaz pikselleri say
    white_pixel_count = np.sum(bottle_area == 255)

    # Eğer bu şişede daha fazla beyaz piksel varsa, onu en iyi şişe olarak kaydet
    if white_pixel_count > max_white_pixels:
        max_white_pixels = white_pixel_count
        best_bottle_x = x_start
        best_bottle_w = bottle_width

# Eğer en iyi şişe bulunmuşsa, onu yeşil dikdörtgenle işaretle
if best_bottle_w > 0:
    image_with_rect = cv2.rectangle(image_rgb.copy(), (best_bottle_x, line_y),
                                    (best_bottle_x + best_bottle_w, image_rgb.shape[0]),
                                    (0, 255, 0), 2)

# Kırmızı çizgiyi ekle
start_point = (0, line_y)
end_point = (image_rgb.shape[1], line_y)
image_with_rect = cv2.line(image_with_rect, start_point, end_point, (255, 0, 0), 2)

# Görüntüyü göster
plt.imshow(image_with_rect)
plt.axis('off')
plt.show()
