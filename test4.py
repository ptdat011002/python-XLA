'''
Đọc ảnh mầu vào biến ma trận I.
Hiển thị ảnh I.
Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức xác định mức độ xám từ tổ hợp
các thành phần mầu (r,g,b), được ma trận ảnh Ig. 
Hiển thị ảnh Ig. 
Xác định mức xám lớn nhất của ảnh Ig.
'''

import cv2
import numpy as np

I=cv2.imread('cake.jpg')
cv2.imshow('anh dau vao',I)

#đổi BGR sang gray
Ig=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',Ig)

print("mức sáng lớn nhất: ",np.max(Ig))

cv2.waitKey()
cv2.destroyAllWindows()

