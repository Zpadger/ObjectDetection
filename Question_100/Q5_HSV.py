#HSV变换
#说实话，没搞懂

# import cv2
# import numpy as np
#
# #read image
# img=cv2.imread("imori.jpg")
# B=img[:,:,0].copy() #三通道
# G=img[:,:,1].copy()
# R=img[:,:,2].copy()
#
# #RGB->HSV
# Max=max(R,G,B)
# Min=min(R,G,B)
#
# H=0
# if Min==Max:
#     H=0
# if Min==B:
#     H=60 * (G - R) / (Max - Min) + 60
# if Min==R:
#     H=60 * (B - G) / (Max - Min) + 180
# if Min==G:
#     H=60 * (R - B) / (Max - Min) + 300
#
# V=Max
# S=Max-Min
#
# #色相反转(色相值加180)
# H+=180
#
# #RGB色彩空间表示图片
# C=S
# H_=H/60
# X=C*(1-abs(H_%2-1))
#
# if 0<=H_<1:
#     (R,G,B)=(V-C)*(1,1,1)+(C,X,0)
# if 1<=H_<2:
#     (R,G,B)=(V-C)*(1,1,1)+(X,C,0)
# if 2<=H_<3:
#     (R,G,B)=(V-C)*(1,1,1)+(0,C,X)
# if 3<=H_<4:
#     (R,G,B)=(V-C)*(1,1,1)+(0,X,C)
# if 4<=H_<5:
#     (R,G,B)=(V-C)*(1,1,1)+(X,0,C)
# if 5<=H_<6:
#     (R,G,B)=(V-C)*(1,1,1)+(C,0,X)
#
# img[:,:,0]=R
# img[:,:,1]=G
# img[:,:,2]=B
#
# #save result
# cv2.imwrite("out.jpg",img)
# cv2.imshow("result",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float32) / 255.

# RGB > HSV
out = np.zeros_like(img) #np.zeros_like(a)生成与数组a相同shape的全0数组

max_v = np.max(img, axis=2).copy()
min_v = np.min(img, axis=2).copy() #np.max取最大值
min_arg = np.argmin(img, axis=2)

H = np.zeros_like(max_v)

H[np.where(max_v == min_v)] = 0
## if min == B
ind = np.where(min_arg == 0)
H[ind] = 60 * (img[..., 1][ind] - img[..., 2][ind]) / (max_v[ind] - min_v[ind]) + 60
## if min == R
ind = np.where(min_arg == 2)
H[ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180
## if min == G
ind = np.where(min_arg == 1)
H[ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300

V = max_v.copy()
S = max_v.copy() - min_v.copy()

# Transpose Hue
H = (H + 180) % 360

# HSV > RGB

C = S
H_ = H / 60
X = C * (1 - np.abs(H_ % 2 - 1))
Z = np.zeros_like(H)

vals = [[Z, X, C], [Z, C, X], [X, C, Z], [C, X, Z], [C, Z, X], [X, Z, C]]

for i in range(6):
    ind = np.where((i <= H_) & (H_ < (i + 1)))
    out[..., 0][ind] = (V - C)[ind] + vals[i][0][ind]
    out[..., 1][ind] = (V - C)[ind] + vals[i][1][ind]
    out[..., 2][ind] = (V - C)[ind] + vals[i][2][ind]

out[np.where(max_v == min_v)] = 0
out = (out * 255).astype(np.uint8)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
