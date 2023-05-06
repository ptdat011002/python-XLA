

import cv2

import numpy as np

# Đọc ảnh mầu watch.jpg vào biến ma trận I.
I = cv2.imread('banh.jpg')

# 1. (2 điểm) Hiển thị kênh B của ảnh I.
cv2.imshow("1",I[:,:,2])

# 2. (4 điểm) Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh S của Ihsv. Xác định giá trị mức sáng trung bình của kênh V của ảnh Ihsv.
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
print("Giá trị mức sáng trung bình của kênh V: ", np.mean(Ihsv[:,:,2]))

# 3. (1 điểm) Làm trơn ảnh kênh S của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 5x5 được ảnh Is. Hiển thị ảnh Is.
Is = cv2.blur(Ihsv[:,:,1], (5,5))
cv2.imshow("2",Is)

# 4. (1.5 điểm) Nhị phân hóa ảnh Is theo ngưỡng Otsu được ảnh nhị phân Ib.Xác định đường contour có chu vi lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh I.
_, Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max_per = 0.0
for cnt in contours:
  if cv2.arcLength(cnt, True) > max_per:
    max_per = cv2.arcLength(cnt, True)
    max_cnt = cnt
I_copy = I.copy()
cv2.drawContours(I_copy, [max_cnt], -1 , (255,0,255), 3)
cv2.imshow("3",I_copy)

# 5. (1.5 điểm) Tăng độ sáng của kênh V của ảnh Ihsv bằng phương pháp giãn tuyến tính các giá trị mức xám. Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I. Hiển thị lại ảnh I.
def gian_muc_xam(Igray):
  h = Igray.shape[0]
  w = Igray.shape[1]
  a = np.min(I)
  b = np.max(I)

  aG = np.zeros(256, dtype= 'uint8')
  for i in range(256): 
    aG[i] = (256 * i) 
  for i in range(h):
    for j in range(w):
      g = Igray[i][j]
      Igray[i][j] = aG[g] 
  return a,b,Igray

av,bv, I[:,:,2] = gian_muc_xam(I[:,:,2])
I_new = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("4",I_new)
cv2.waitKey()
cv2.destroyAllWindows()