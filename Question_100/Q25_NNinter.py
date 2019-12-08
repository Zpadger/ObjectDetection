import cv2
import numpy as np
import matplotlib.pyplot as plt


# Nereset Neighbor interpolation
def nn_interpolate(img, ax=1, ay=1):
    H, W, C = img.shape

    aH = int(ay * H)
    aW = int(ax * W)

    y = np.arange(aH).repeat(aW).reshape(aW, -1)
    x = np.tile(np.arange(aW), (aH, 1))
    y = np.round(y / ay).astype(np.int)
    x = np.round(x / ax).astype(np.int)

    out = img[y,x]

    out = out.astype(np.uint8)

    return out


# Read image
img_original = cv2.imread("imori.jpg")
img = cv2.imread("imori.jpg").astype(np.float)
cv2.imshow("imori",img_original)
while cv2.waitKey(100) != 27:
    if cv2.getWindowProperty('imori',cv2.WND_PROP_VISIBLE) <= 0:
        break

# Nearest Neighbor
out = nn_interpolate(img, ax=1.5, ay=1.5)#放大1.5倍

# Save result
#cv2.imshow("imori",img) #存疑，为啥是白的？--可能是.astype(np.float)
cv2.imshow("result", out)
#cv2.waitKey(0)
while cv2.waitKey(100) != 27:
    if cv2.getWindowProperty('result',cv2.WND_PROP_VISIBLE) <= 0:
        break
cv2.imwrite("out.jpg", out)