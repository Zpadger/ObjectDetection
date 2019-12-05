import cv2
import numpy as np
import matplotlib.pyplot as plt

#histogram normalization
def his_normalization(img,a=0,b=255):
    #get max and min
    c = img.min()
    d = img.max()

    out = img.copy()

    #normalization
    out = (b-a)/(d-c)*(out-c)+a
    out[out<a]=a
    out[out>b]=b
    out = out.astype(np.uint8)

    return out

#read image
img = cv2.imread("imori_dark.jpg").astype(np.float)
H, W, C =img.shape

#histogram normalization
out = his_normalization(img)

#display histogram
plt.hist(out.ravel(),bins=255,rwidth=0.8,range=(0,255))#返回的是视图，可以修改out的值
plt.savefig("out_his.png")
plt.show()

# #save result
# cv2.imshow("result",out)
# cv2.waitKey(0)
# cv2.imwrite("out.jpg",out)