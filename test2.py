'''
Đọc ảnh mầu vào biến ma trận I. 
Hiển thị giá trị độ cao và độ rông của ảnh I và cả ảnh I.
Hiệu chỉnh lại ảnh I với size mới là độ cao 256, độ rộng 256 được ảnh I2. Hiển thị ảnh I2.
Chuyển đôi ảnh I sang ảnh HSV được ma trận ảnh Ihsv. Hiển thị kênh H của ảnh Ihsv.
'''

import cv2
import numpy as np

I=cv2.imread('cake.jpg')
c
cv2.imshow('anh dau vao',I)

I2=cv2.resize(I,(256,256))#do rong,do cao
cv2.imshow('anh co gian',I2)

Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
cv2.imshow("kenh H", Ihsv[:, :, 0])
#min,max,trung bình độ sáng của kênh V
print('Độ sáng min, max, trung bình của kênh V')
print(np.min(Ihsv[:,:,2]),np.max(Ihsv[:,:,2]),np.mean(Ihsv[:,:,2]))

cv2.waitKey()
cv2.destroyAllWindows()