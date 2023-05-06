import cv2
import numpy as np

I = cv2.imread("cake.jpg")
TBC = (I[:,:,2]+I[:,:,0]) / 2
cv2.imshow("TBC cau 2 kenh R va B",TBC)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow("kenh H", Ihsv[:,:,0]) 
print("mức sáng lớn nhất kênh S:", np.max(Ihsv[:,:,1]))

# 3. (1 điểm) Làm trơn ảnh kênh S của Ihsv theo bộ lọc trung bình cộng, kích thước cửa sổ lân cận là 7x7 được ảnh Is. Hiển thị ảnh Is.
Is = cv2.blur(Ihsv[:,:,1], (7,7))
cv2.imshow("anh Is",Is)

# 4. (1.5 điểm) Nhị phân hóa của ảnh 255-Is theo ngưỡng Otsu được ảnh nhị phân Ib.
_, Is = cv2.threshold(Is, 0, 255, cv2.THRESH_OTSU)
Ib = 255 - Is
cv2.imshow("anh nhi phan",Ib)

# Xác định đường contour có chu vi lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh gôc I và hiển thị ảnh I.
coutours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max = 0.0
max_per = []
for cnt in coutours:
  if cv2.arcLength(cnt, True) > max:
    max = cv2.arcLength(cnt,True)
    max_per = cnt
I_copy = I.copy()
cv2.drawContours(I_copy,[cnt], -1, 255, 2)
cv2.imshow("contours",I_copy)

# 5. (1.5 điểm) Tăng độ sáng của kênh V của ảnh Ihsv bằng phương pháp giãn tuyến tính mức xám. Biến đổi ngược ảnh Ihsv về biểu diễn mầu RGB được ảnh I mới.
def gian_muc_xam(Igray):
    w=Igray.shape[1]
    h=Igray.shape[0]
    a=np.min(Igray)
    b=np.max(Igray)
    print([a,b])
    #chinh lai
    aG=np.zeros(256,dtype='uint8')
    for g in range(256):
      aG[g] = (255* g)//(b-a)
    for i in range(h):
      for j in range(w):
          g=Igray[i][j] 
          Igray[i][j]=aG[g]
    return a,b,Igray

I[:,:,2],_,_ = gian_muc_xam(I[:,:,2])
I_new = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("anh moi",I_new)
cv2.waitKey()
cv2.destroyAllWindows()

