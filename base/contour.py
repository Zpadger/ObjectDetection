import cv2

img=cv2.imread("cola.jpg")#读取图片
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#颜色空间转换函数
gray=cv2.GaussianBlur(gray,(3,3),0)#高斯滤波 输入为 图像 高斯矩阵尺寸 标准差
gray=cv2.Canny(gray,100,300)#边缘检测 最小值 最大值

ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#阈值函数 图片源 起始值 最大值 算法类型
contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#检索轮廓
#ValueError: not enough values to unpack (expected 3, got 2)
#cv2中的findContours现在只能返回两个值
cv2.drawContours(img,contours,-1,(0,0,0),2)#轮廓绘制或填充

cv2.imshow("contour1",binary)
cv2.imwrite("contour1.jpg",binary)
cv2.imshow("contour2",img)
cv2.imwrite("contour2.jpg",img)

cv2.waitKey()
