#通道交换
#读取图像，然后将RGB通道替换成BGR通道
#cv2.imread()按照BGR顺序排列

import cv2

#read image
img=cv2.imread("imori.jpg")
blue=img[:,:,0].copy() #三通道
green=img[:,:,1].copy()
red=img[:,:,2].copy()

#write image
#RGB -> BGR
img[:,:,0]=red
img[:,:,1]=green
img[:,:,2]=blue

#save result
cv2.imwrite("out.jpg",img)
cv2.imshow("result",img)
cv2.waitKey()
cv2.destroyAllWindows()
