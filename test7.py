import numpy as np
from matplotlib import pyplot as plt
import cv2

# Đọc ảnh mầu vào biến ma trận I.
I = cv2.imread('cake.jpg')
# 1. (2 điểm) Hiển thị kênh B của ảnh I.
cv2.imshow("kenh B",I[:,:,0])
# 2. (4 điểm) Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh S của Ihsv. Xác định giá trị mức sáng trung bình của kênh V của ảnh Ihsv.
Ihsv = cv2.cvtColor(I, cv2.COLOR_RGB2HSV)
cv2.imshow("kenh S",Ihsv[:,:,1])
print("Mức sáng trung bình của Kênh V:", np.mean(Ihsv[:,:,2]))

# 3. (1 điểm) Làm trơn ảnh kênh S của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 5x5 được ảnh Is. Hiển thị ảnh Is.
Is = cv2.blur(Ihsv[:,:,1],(5,5))
cv2.imshow("lam tron kenh S",Is)

# 4. (1.5 điểm) Nhị phân hóa ảnh Is theo ngưỡng Otsu được ảnh nhị phân Ib.
thr, Ib = cv2.threshold(Is,0,255,cv2.THRESH_OTSU)
cv2.imshow("anh nhi phan",Ib)

# Xác định đường contour có chu vi lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh I.
contours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max_per = 0.0
for cnt in contours:
    if max_per <= cv2.arcLength(cnt, True):
        max_per = cv2.arcLength(cnt, True)
        contour_max = cnt
cv2.drawContours(I, [contour_max], -1, 255, 2)
cv2.imshow("contour",I) 

# 5. (1.5 điểm) Tăng độ sáng của kênh V của ảnh Ihsv bằng phương pháp giãn tuyến tính các giá trị mức xám. Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I. Hiển thị lại ảnh I.
def gian_muc_xam(Igray):
    w=Igray.shape[1]
    h=Igray.shape[0]
    a=np.min(Igray)
    b=np.max(Igray)
    print([a,b])
    aG=np.zeros(256,dtype='uint8')
    for g in range(256):
      aG[g]=(255* g)//(b-a)
    for i in range(h):
        for j in range(w):
            g=Igray[i][j]
            Igray[i][j]=aG[g]
    return a,b,Igray

av,bv,Ihsv[:,:,2]=gian_muc_xam(Ihsv[:,:,2])

I2 = cv2.cvtColor(Ihsv,cv2.COLOR_HSV2RGB)
cv2.imshow("tang do sang",I2)

cv2.waitKey()
cv2.destroyAllWindows()