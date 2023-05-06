
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Đọc ảnh mầu apple.jpg vào biến ma trận I.
I = cv2.imread('banh.jpg')

# 1. (2 điểm) Hiển thị kênh R của ảnh I.
cv2.imshow("1",I[:,:,2])

# 2. (4 điểm) Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức xác định mức độ xám từ tổ hợp các thành phần mầu (r,g,b) theo tỷ lệ (0.39,0.5,0.11), được ma trận ảnh Ig. Hiển thị ảnh Ig. Xác định mức xám trung bình của ảnh Ig.
def to_Gray(I):
  Ig = 0.39 *I[:,:,2] + 0.5 * I[:,:,1] + 0.11 * I[:,:,0]
  Ig = Ig.astype('uint8')
  return Ig

Ig = to_Gray(I)
cv2.imshow("2",Ig)

# 3. (1 điểm) Xác định ma trận gradient theo hướng x của Ig sử dụng toán tử Sobel và hiển thị ma trận kết quả.
gradientX = cv2.Sobel(Ig, cv2.CV_64F, 1, 0, 3)
plt.subplot(2,2,1)
plt.imshow(gradientX,cmap = 'gray')
plt.title('Sobel X')
plt.xticks([])
plt.yticks([])
plt.show()

# 4. (1 điểm) Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Kiểm tra các điểm ảnh của pixel có tọa độ dòng  y=100, cột x=120 có phải là điểm biên của Ig theo phương pháp dò biên Canny.
Ie = cv2.Canny(Ig, 0, 255)
y = 100
x = 120
if Ie[y][x] == 255:
  print("Điểm ảnh của pixel có tọa độ dòng  "+str(y)+", cột "+str(x)+" là điểm biên của Ig theo phương pháp dò biên Canny")
else:
  print("Điểm ảnh của pixel có tọa độ dòng  "+str(y)+", cột "+str(x)+" không phải là điểm biên của Ig theo phương pháp dò biên Canny")

# 5. (1.5 điểm). Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen Ib. Xác đường contour của ảnh Ib có diện tích lớn nhất. Vẽ đường contour tìm được trên lên ảnh gốc I.
_, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max = 0.0
max_area = []
for cnt in contours:
  if max <= cv2.contourArea(cnt):
    max = cv2.contourArea(cnt)
    max_area = cnt
I_copy = I.copy()
cv2.drawContours(I_copy, [max_area], -1, 255, 3)
cv2.imshow("3",I_copy)
cv2.waitKey()
cv2.destroyAllWindows()