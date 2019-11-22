#均值滤波

import cv2
import numpy as np

#read image
img=cv2.imread("imori.jpg")
h,w,c=img.shape

#mean filter
K_size=3

#zero padding
pad=K_size//2
out=np.zeros((h+pad*2,w+pad*2,c),dtype=np.float)
out[pad:pad+h,pad:pad+w]=img.copy().astype(np.float)

tmp=out.copy()

for y in range(h):
    for x in range(w):
        for c in range(c):
            out[pad+y,pad+x,c]=np.mean(tmp[y:y+K_size,x:x+K_size,c]) #取所有元素平均值

out=out[pad:pad+h,pad:pad+w].astype(np.uint8)

#save result
cv2.imwrite("out.jpg",out)
cv2.imshow("result",out)
cv2.waitKey(0)
cv2.destroyAllWindows()