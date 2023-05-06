'''
Đọc ảnh mầu vào biến ma trận I.
Hiển thị ảnh I.
Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh H của Ihsv.
Xác định giá trị mức sáng nhỏ nhất của kênh S của ảnh Ihsv.
'''

import cv2
import numpy as np

I=cv2.imread('cake.jpg')
#3a
cv2.imshow('anh vao',I)
#3b
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
cv2.imshow('kenh H',Ihsv[:,:,0])
#cv2.imshow('kenh S',Ihsv[:,:,1])
#cv2.imshow('kenh V',Ihsv[:,:,2])
#mức sáng min
print("mức sáng nhỏ nhất của kênh S của ảnh Ihsv")
print(np.min(Ihsv[:,:,1]))


cv2.waitKey()
cv2.destroyAllWindows()


