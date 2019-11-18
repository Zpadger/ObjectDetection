#图像二值化

import cv2
import numpy as np

#read image
img=cv2.imread("imori.jpg").astype(np.float)
b=img[:,:,0].copy()
g=img[:,:,1].copy()
r=img[:,:,2].copy()

#thresholding
# y=0.2126*r+0.7152*g+0.0722*b
# y=y.astype(np.uint8)
#
# if y<128:
#     y=0
# else:
#     y=255
# #ValueError: The truth value of an array with more than one element is ambiguous.
# # Use a.any() or a.all()



#Gray scale
out=0.2126*r+0.7152*g+0.0722*b
out=out.astype(np.uint8)

#Binarization
th=128
out[out<128]=0
out[out>=128]=255

#Numpy的内置索引，arr[arr>255]=x表示将所有＞255的元素替换为x
#https://vimsky.com/article/3727.html

#save result
cv2.imwrite("out.jpg",out)
cv2.imshow("result",out)
cv2.waitKey(0)
cv2.destroyAllWindows()

#ValueError: The truth value of an array with more than one element is ambiguous.
# Use a.any() or a.all()