#Max-Min Filter
#用于边缘检测

import cv2
import numpy as np

img=cv2.imread("imori.jpg")
h,w,c=img.shape

#filter
K_size=3

K=np.diag([1]*K_size).astype(np.float)
K/=K_size

#zero padding
pad=K_size//2
out=np.zeros((h+pad*2,w+pad*2,c),dtype=np.float)
out[pad:pad+h,pad:pad+w]=img.copy().astype(np.float)

tmp=out.copy()

for y in range(h):
    for x in range(w):
        for c in range(c):
            out[pad+y,pad+x,c]=np.max(tmp[y:y+K_size,x:x+K_size,c])\
                               -np.min(tmp[y:y+K_size,x:x+K_size,c])


out = out[pad:pad+h, pad:pad+w].astype(np.uint8)

#save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()