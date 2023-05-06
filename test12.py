'''Đọc ảnh mầu hat1.png vào biến ma trận I.
1. (2 điểm) Hiển thị kênh B của ảnh I.
2. (4 điểm) Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh H của Ihsv. Xác định giá trị mức sáng trung bình của kênh S của ảnh Ihsv.
3. (1 điểm) Xác định và vẽ histogram của kênh S của ảnh Ihsv.
4. (1.5 điểm) Làm trơn ảnh kênh V của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 3x3 được ảnh Is. Hiển thị các giá trị mức xám trong lân cận 5x5 của điểm ảnh có tọa độ dòng y=9, cột x=11.
5. (1.5 điểm) Nhị phân hóa ảnh Is theo ngưỡng Otsu được ảnh nhị phân Ib.
Xác định đường contour có chu vi lớn nhất của ảnh Ib. Vẽ đường contour đó trên ảnh gôc I.'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

I = cv2.imread("cake.jpg")
cv2.imshow("kenh B", I[:,:,0])

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("kenh H cua anh Ihsv", Ihsv[:,:,0])
print("mức sáng trung bình của kênh S ảnh Ihsv:",np.mean(Ihsv[:,:,1]))

def tinh_his(I_new):
  h = I_new.shape[0]
  w = I_new.shape[1]
  mang_hist = np.zeros(256, dtype ='uint32')
  for i in range(h):
    for j in range(w):
      g = I_new[i][j]
      mang_hist[g] = mang_hist[g] + 1
  return mang_hist

hist_S = tinh_his(Ihsv[:,:,1])
plt.plot(hist_S)
plt.show()

Is = cv2.blur(Ihsv[:,:,1], (3,3))
height = Is.shape[0]
width = Is.shape[1]
y=100
x=150
for k in range(-1,6): 
  for l in range(-1,6):
    if ((y + k )>= 0 & ((y + k) <= height - 1)) & ((x + l)>=0) &((x + l ) <= width - 1):
      print("Các mức độ xám của của sổ lân cận 7x7 điểm ảnh (y="+str(y)+",x="+str(x)+")",Ihsv[y + k, x + l])

_, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_OTSU)
contours,_ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max = 0.0
max_contours = []
for cnt in contours:
  if max <= cv2.arcLength(cnt,True):
    max = cv2.arcLength(cnt,True)
    max_contours = cnt
I_copy = I.copy()
cv2.drawContours(I_copy, [max_contours], -1, 255, 3)
cv2.imshow("I",I_copy)

cv2.waitKey()
cv2.destroyAllWindows()