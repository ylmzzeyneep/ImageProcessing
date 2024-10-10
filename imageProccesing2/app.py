import numpy as np
import random
import cv2
from sklearn.neighbors import KNeighborsClassifier

# Gri tonlamalı görüntüyü yükle
image_path = 'images/img.jpg'  # Görüntü dosya yolunu buraya yazın
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Görüntünün boyutlarını al
height, width = image.shape

# Görüntüyü piksel değerlerinin 2D dizisine dönüştür
pixels = image.reshape(-1, 1)  # Şekil: (piksel_sayısı, 1)

# Rastgele bir piksel indeksi seç
random_index = random.randint(0, pixels.shape[0] - 1)
selected_pixel_value = pixels[random_index][0]
selected_coordinates = (random_index // width, random_index % width)

# Komşu sayısını belirle (m)
m = 8  # Daha fazla veya daha az komşu almak için bu değeri değiştirebilirsiniz

# k-NN modeli için verileri hazırla
# Her piksel için koordinat özelliklerini oluştur
X = np.array([(i // width, i % width) for i in range(pixels.shape[0])])  # Şekil: (piksel_sayısı, 2)
y = pixels.flatten()  # Piksel değerlerini hedef olarak düzleştir

# k-NN modelini başlat ve eğit
knn = KNeighborsClassifier(n_neighbors=m)
knn.fit(X, y)

# Seçilen pikselin koordinatlarını kullanarak m en yakın komşusunu bul
neighbors_indices = knn.kneighbors([selected_coordinates], return_distance=False)

# Sonuçları yazdır
print("Seçilen Piksel Koordinatları:", selected_coordinates)
print("Seçilen Piksel Değeri:", selected_pixel_value)
print("En Yakın Komşu İndeksleri:", neighbors_indices[0])

# En yakın komşuların değerlerini yazdır
print("En Yakın Komşu Piksel Değerleri:")
for idx in neighbors_indices[0]:
    print("Piksel Koordinatları:", (idx // width, idx % width), "Değer:", pixels[idx][0])
