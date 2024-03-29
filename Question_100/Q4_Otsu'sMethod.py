#大津二值化算法
#得到使类间方差最大的阈值T

import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float)

H, W, C = img.shape

# Grayscale
out = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
out = out.astype(np.uint8)

# Determine threshold of Otsu's binarization
max_sigma = 0
max_t = 0

for _t in range(1, 255):
    v0 = out[np.where(out < _t)] #np.where(condition)输出满足条件元素的坐标
    m0 = np.mean(v0) if len(v0) > 0 else 0. #np.mean()根据制定轴方向计算算术平均值
    w0 = len(v0) / (H * W)
    v1 = out[np.where(out >= _t)]
    m1 = np.mean(v1) if len(v1) > 0 else 0.
    w1 = len(v1) / (H * W)
    sigma = w0 * w1 * ((m0 - m1) ** 2) #类间方差

    #确定最大类间方差的阈值t
    if sigma > max_sigma:
        max_sigma = sigma
        max_t = _t

# Binarization
print("threshold >>", max_t)
th = max_t
out[out < th] = 0
out[out >= th] = 255

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
