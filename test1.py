'''
Đọc ảnh mầu vào biến ma trận I.
Hiển thị kênh G của ảnh I.
Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo phương pháp tổ hợp 3 thành phần mầu, được ma trận ảnh Ig.
Hiển thị ảnh Ig và hiển thị giá trị đô cao, độ rộng của ảnh Ig.
'''

import cv2
import numpy as np

I=cv2.imread('cake.jpg')
cv2.imshow('kenh G',I[:,:,1]) # OpenCV: BGR:0->B,1->G,2->R

#đổi BGR sang gray
Ig=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
so_dong=I.shape[0]
so_cot=I.shape[1]
Ig=np.zeros((so_dong,so_cot),dtype='uint8')
for i in range(so_dong):
    for j in range(so_cot):
        #gray=0.39*r+0.50*g+0.11*b
        d=39*int(I[i][j][2]) + 50*int(I[i][j][1]) + 11*int(I[i][j][0])
        d=d//100
        Ig[i][j]=d
cv2.imshow('Gray',Ig)

print("độ cao ảnh ",Ig.shape[0])
print("độ rộng ảnh ",Ig.shape[1])

cv2.waitKey()
cv2.destroyAllWindows()