import cv2
import numpy as np

# Đọc ảnh mầu vào biến ma trận I.
I = cv2.imread('cake.jpg')
# 1. (2 điểm) Hiển thị kênh B của ảnh I.
cv2.imshow("kenh B",I[:,:,0])
# 2. (4 điểm) Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức xác định mức độ xám từ tổ hợp các thành phần mầu (r,g,b) theo tỷ lệ (0.39,0.5,0.11),
def to_Gray(I):
  Ig = 0.39*I[:,:,2] + 0.5*I[:,:,1] + 0.11*I[:,:,0]
  Ig = Ig.astype('uint8')
  return Ig
Ig = to_Gray(I)
cv2.imshow("anh da cap xam",Ig)
# 3. (1 điểm). Chuyển ảnh Ig sang ảnh nhị phân Ib với ngưỡng Otsu.
_, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("anh nhi phan",Ib)
# 4. (1.5 điểm). Làm trơn ảnh Ig theo bộ lọc trung bình cộng với lân cận cửa sổ kích thước 5x5 thu được ảnh Im.
Im = cv2.blur(Ig, (5,5))
cv2.imshow("lam tron anh",Im)
# 5. (1.5 điểm). Xác định các contour của ảnh Im và vẽ vị trí các contour lên ảnh gốc I ban đầu.
I_copy = I.copy()
_,Ibm = cv2.threshold(Im, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(Ibm, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy, contours, -1, 255, 3)
cv2.imshow("",I_copy)
cv2.waitKey()
cv2.destroyAllWindows()
