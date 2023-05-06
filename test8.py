import numpy as np
import cv2
from matplotlib import pyplot as plt

# Đọc ảnh mầu vào biến ma trận I.
I = cv2.imread('cake.jpg')

# 1. (2 điểm) Hiển thị kênh R của ảnh I.
cv2.imshow("kenh R",I[:,:,2])

# 2. (4 điểm) Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức xác định mức độ xám từ tổ hợp các thành phần mầu (r,g,b) theo tỷ lệ (0.39,0.5,0.11), được ma trận ảnh Ig. Hiển thị ảnh Ig. Xác định mức xám trung bình của ảnh Ig.
def to_Gray(I):
  Ig = 0.39 * I[:,:,2] + 0.5  * I[:,:,1] + 0.11 * I[:,:,0]
  Ig = Ig.astype(dtype ='uint8')
  return Ig
Ig = to_Gray(I)
cv2.imshow("anh Ig",Ig)
print("muc xam trung binh cua anh Ig: ",np.mean(Ig))

# 3. (1 điểm) Xác định ma trận gradient theo hướng x của Ig sử dụng toán tử Sobel và hiển thị ma trận kết quả.
IgradientX = cv2.Sobel(Ig, cv2.CV_64F, 1, 0, 3)
plt.subplot(2, 2, 1), plt.imshow(IgradientX, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.show()

# 4. (1 điểm) Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Kiểm tra các điểm ảnh của pixel có tọa độ dòng  y=100, cột x=120 có phải là điểm biên của Ig theo phương pháp dò biên Canny.
Ie = cv2.Canny(Ig, 0, 255)
if Ie[100][120] == 255:
    print("diem anh Igray(y=100,x=120) la diem bien theo Canny")
else:
    print("diem anh Igray(y=100,x=120) ko la điem bien theo Canny")
    
# 5. (1.5 điểm). Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen Ib. Xác đường contour của ảnh Ib có diện tích lớn nhất. Vẽ đường contour tìm được trên lên ảnh gốc I.
thr, Ib = cv2.threshold(Ig, 0,255, cv2.THRESH_OTSU)
contours,_ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max_area = 0.0
contour_max = []
for cnt in contours:
  if max_area < cv2.contourArea(cnt):
    max_area = cv2.contourArea(cnt)
    contour_max = cnt

cv2.drawContours(I, [contour_max], -1, (0,255,0), 2)
cv2.imshow("anh nhi phan",I)

cv2.waitKey()
cv2.destroyAllWindows();