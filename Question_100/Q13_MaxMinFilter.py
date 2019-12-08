#Max-Min Filter
#用于边缘检测

import cv2
import numpy as np

# img=cv2.imread("imori.jpg")
# h,w,c=img.shape

# #filter
# K_size=3

# K=np.diag([1]*K_size).astype(np.float)
# K/=K_size

# #zero padding
# pad=K_size//2
# out=np.zeros((h+pad*2,w+pad*2,c),dtype=np.float)
# out[pad:pad+h,pad:pad+w]=img.copy().astype(np.float)

# tmp=out.copy()

# for y in range(h):
#     for x in range(w):
#         for c in range(c):
#             out[pad+y,pad+x,c]=np.max(tmp[y:y+K_size,x:x+K_size,c])\
#                                -np.min(tmp[y:y+K_size,x:x+K_size,c])


# out = out[pad:pad+h, pad:pad+w].astype(np.uint8)

# Gray scale
def BGR2GRAY(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    # Gray scale
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = out.astype(np.uint8)

    return out

# max-min filter
def max_min_filter(img, K_size=3):
    #H, W, C = img.shape
    H, W =img.shape

    # Zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = gray.copy().astype(np.float)
    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            out[pad + y, pad + x] = np.max(tmp[y: y + K_size, x: x + K_size]) - np.min(tmp[y: y + K_size, x: x + K_size])

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out


# Read image
img = cv2.imread("imori.jpg").astype(np.float)

#BGR2GRAY函数简写
#BGR转GRAY不用自写的函数，直接调用opencv中的转换函数
#img = cv2.imread("imori.jpg").astype(np.float32)

#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# grayscale
gray = BGR2GRAY(img)

# Max-Min filtering
out = max_min_filter(gray, K_size=3)

#save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
