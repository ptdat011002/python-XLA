import cv2
import numpy as np
from matplotlib import pyplot as plt

# Đọc ảnh mầu vào biến ma trận I.
I = cv2.imread('cake.jpg')

# 1. (2 điểm) Hiển thị tỷ lệ giữa giá trị độ cao và độ rông của ảnh I.
height = I.shape[0]
width = I.shape[1]
print("Tỷ lệ giữa giá trị độ cao và độ rộng của ảnh: ", width/height)

# 2. (4 điểm) Hiệu chỉnh lại ảnh I với size mới là độ cao 256, độ rộng 256 được ảnh mới I2. Hiển thị ảnh I2.
I2 = cv2.resize(I, (256,256))
cv2.imshow("anh chinh sua",I2)

# 3. (1 điểm) Chuyển đôi ảnh I sang ảnh HSV được ma trận ảnh Ihsv. Hiển thị kênh S của ảnh Ihsv.
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("kenh S",Ihsv[:,:,1])

# 4. (1.5 điểm) Xác định biên theo phương pháp Canny của kênh V của ảnh Ihsv được ảnh nhị phân Ivb.
Ivb = cv2.Canny(Ihsv[:,:,2], 0, 255)
cv2.imshow("anh nhi phan",Ivb)
cv2.waitKey()
cv2.destroyAllWindows()

# 5. (1.5 điểm) Xác định histogram của kênh S của ảnh Ihsv.
def tinh_his(I):
  h = I.shape[0]
  w = I.shape[1]
  mang_hist = np.zeros(256, dtype = 'uint32')
  for i in range(h):
    for j in range(w):
      g = I[i][j]
      mang_hist[g] = mang_hist[g] + 1
  return mang_hist
hist_S = tinh_his(Ihsv[:,:,1])
plt.plot(hist_S)
plt.show()