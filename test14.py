
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Đọc ảnh mầu hat1.png vào biến ma trận I.
I = cv2.imread('cake.jpg')

# 1. (2 điểm) Hiển thị kênh ảnh B của I.
cv2.imshow("kenh B",I[:,:,2])

# 2. (4 điểm) Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh V của Ihsv. Xác định giá trị mức sáng trung bình của kênh S của ảnh Ihsv
Ihsv = cv2.cvtColor(I, cv2.COLOR_RGB2HSV)
cv2.imshow("kênh V",Ihsv[:,:,2])
print("Mức sáng trung bình của Kênh S: ", np.mean(Ihsv[:,:,1]))

# 3. (1 điểm) Xác định và vẽ histogram của kênh V của ảnh Ihsv.
def tinh_his(Igray):
    w=Igray.shape[1]
    h=Igray.shape[0]

    mang_hist = np.zeros( 256,dtype='uint32')
    for i in range(h):
        for j in range(w):
            g=Igray[i][j]
            mang_hist[g]=mang_hist[g]+1
    return mang_hist
hist_V = tinh_his(Ihsv[:,:,2])
plt.plot(hist_V)
plt.show()

# 4. (1.5 điểm) Làm trơn ảnh kênh S của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 5x5 được ảnh Is. Hiển thị ảnh Is.
Is = cv2.blur(Ihsv[:,:,1],(5,5))
cv2.imshow("kênh S",Is)

# 5. (1.5 điểm) Xác định đường contour có tỉ lệ giữa chu vi và diện tích là lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh gôc I Hiển thị ảnh I
Ig = cv2.cvtColor(I, cv2.COLOR_RGB2GRAY)
_, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
coutours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max = 0.0
for cnt in coutours:
   if cv2.arcLength(cnt, True) != 0 and (cv2.contourArea(cnt)) != 0:
    ti_so = (cv2.arcLength(cnt, True))/(cv2.contourArea(cnt))
    if ti_so > max:
          max = ti_so
          contour_max = cnt
I_copy = I.copy()
cv2.drawContours(I_copy,[contour_max], -1, 255, 2)
cv2.imshow("anh I",I_copy)

cv2.waitKey()
cv2.destroyAllWindows()