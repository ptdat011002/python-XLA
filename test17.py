
import cv2
import numpy as np

# 1. (2 điểm) Hiển thị ảnh I.
I = cv2.imread('cake.jpg')

# 2. (4 điểm) Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức xác định mức độ xám từ tổ hợp các thành phần mầu (r,g,b) theo tỷ lệ (0.39,0.5,0.11), được ma trận ảnh Ig. Hiển thị ảnh Ig. Xác định mức xám trung bình của ảnh Ig.
def to_Gray(I):
  Ig = 0.39 * I[:,:,2] + 0.5 * I[:,:,1] + 0.11 *I[:,:,0]
  Ig = Ig.astype('uint8')
  return Ig

Ig = to_Gray(I)
cv2.imshow("anh xam",Ig)

# 3. (1 điểm) Hiển thị các độ xám của của cửa sổ lân cận 5x5 của pixel có tọa độ dòng y=100, cột x=120 của ảnh Ig.
height = Ig.shape[0]
width = Ig.shape[1]
y = 100
x = 150
for k in range(-1, 6):
    for l in range(-1, 6):
        if ((y + k) >= 0) & ((y + k) <= height - 1) & ((x + l) >= 0) & ((x + l) <= width - 1):
            print("Các mức độ xám của của sổ lân cận 7x7 điểm ảnh Igray(y=100,x=120)",Ig[y + k, x + l])

# 4. (1.5 điểm) Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Hiển thị ảnh Ie. Kiểm tra
Ie = cv2.Canny(Ig, 0, 255)
if Ie[109][130] == 255:
  print('Điểm ảnh của pixel có tọa độ dòng  y=109, cột x=130 là điểm biên của Ig theo phương pháp dò biên Canny. ')
else:
  print('Điểm ảnh của pixel có tọa độ dòng  y=109, cột x=130 không phải là điểm biên của Ig theo phương pháp dò biên Canny. ')

# 5. (1.5 điểm). Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen Ib. Xác định các đường contour của ảnh Ib gần tương tự với đường tròn. Vẽ các đường contour trên lên ảnh gốc I. Hiển thị ảnh I.
I_copy = I.copy()
_,Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(Ib, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy, contours, -1, 255, 3)
cv2.imshow("contours",I_copy)
cv2.waitKey()
cv2.destroyAllWindows()