import cv2
import numpy as np
import matplotlib.pyplot as plt

#histogram manipulation
def his_man(img,m0=128,s0=52):
    m = np.mean(img)
    s = np.std(img)

    out = img.copy()

    #normalize
    out = s0/s*(out-m)+m0
    out[out<0] = 0
    out[out>255] = 255
    out = out.astype(np.uint8)

    return out


#read image
img = cv2.imread("imori_dark.jpg").astype(np.float)

#histogram normalization
out = his_man(img)

#display histogram
plt.hist(out.ravel(),bins=255,rwidth=0.8,range=(0,255))#返回的是视图，可以修改out的值
plt.savefig("out_his.png")
plt.show()

# #save result
# cv2.imshow("result",out)
# cv2.waitKey(0)
# cv2.imwrite("out.jpg",out)