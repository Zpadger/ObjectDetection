#图像灰度化
#Y = 0.2126 R + 0.7152 G + 0.0722 B
#Wrong answer

# import cv2
#
# #read image
# img=cv2.imread("imori.jpg")
# B=img[:,:,0].copy()
# G=img[:,:,1].copy()
# R=img[:,:,2].copy()
#
# #Gray scale
# #Y = 0.2126 R + 0.7152 G + 0.0722 B
# img[:,:,0]=0.0722*B
# img[:,:,1]=0.7152*G
# img[:,:,2]=0.2126*R
#
# #save result
# cv2.imwrite("out.jpg",img)
# cv2.imshow("result",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#correct answer

import cv2
import numpy as np

#read image
img=cv2.imread("imori.jpg").astype(np.float) #img为什么变成白纸了
b=img[:,:,0].copy()
g=img[:,:,1].copy()
r=img[:,:,2].copy()

#Gray scale
out=0.2126*r+0.7152*g+0.0722*b
out=out.astype(np.uint8)

#save result
cv2.imwrite("out.jpg",out)
cv2.imshow("result",out)
cv2.waitKey(0)
cv2.destroyAllWindows()
