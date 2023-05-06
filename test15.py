
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Đọc ảnh mầu I04.jpg vào biến ma trận I.
I = cv2.imread('cake.jpg')

# 1. (2 điểm) Hiển thị tỷ lệ giữa giá trị độ cao và độ rông của ảnh I.
h = I.shape[0]
w = I.shape[1]
print("tỉ lệ: ", h/w)


# 2. (4 điểm) Hiệu chỉnh lại ảnh I với size mới là độ cao 256, ảnh giữ nguyên tỷ lệ so với ảnh gốc, được ảnh mới I2. Hiển thị ảnh I2.
new_Height = 256
W = w * new_Height // h 
I2 = cv2.resize(I,(W,new_Height))
cv2.imshow("anh da chinh sua",I2)

# 3. (1 điểm) Chuyển đôi ảnh I sang ảnh HSV được ma trận ảnh Ihsv. Hiển thị kênh S của ảnh Ihsv.
Ihsv = cv2.cvtColor(I, cv2.COLOR_RGB2HSV)
cv2.imshow("kenh S",Ihsv[:,:,1])

# 4. (1.5 điểm) Làm trơn kênh S của ảnh Ihsv với bộ lọc median kích thước cửa sổ 3x3. Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I3. Hiển thị ảnh I3.
Ihsv[:,:,1] = cv2.medianBlur(Ihsv[:,:,1], 3)
I3 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2RGB)
cv2.imshow("anh I3",I3)

# 5. (1.5 điểm) Cân bằng histogram của kênh S của ảnh Ihsv. Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I4. Hiển thị ảnh I4.
Ihsv[:,:,1] = cv2.equalizeHist(Ihsv[:,:,1])
I4 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2RGB)
cv2.imshow("anh I4",I4)
cv2.waitKey()
cv2.destroyAllWindows()