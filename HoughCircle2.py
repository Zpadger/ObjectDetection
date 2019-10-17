#循环显示存在问题
import  cv2

src = cv2.imread('footbals.jpg')
cv2.imshow('src_img',src)
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

# 输出图像大小，方便根据图像大小调节minRadius和maxRadius
# 演示 minDist 的值对检测效果的影响
minDists = [100,125,150]
imgcopy = [src.copy(),src.copy(),src.copy()]
for minDist,imgcopy in zip(minDists,imgcopy):
    circles= cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,dp=1,minDist=minDist,param1=100,param2=30,minRadius=20,maxRadius=300)

    print('circles',circles)                         # 查看返回值
    print('len(circles[0])',len(circles[0]))         # 输出检测到圆的个数

    print('-------------------------------------')

    for circle in circles[0]:
        x=int(circle[0])                             # 坐标行列
        y=int(circle[1])
        r=int(circle[2])                             # 半径
        img=cv2.circle(imgcopy,(x,y),r,(0,0,255),2)  # 在原图用指定颜色标记出圆的位置
    cv2.imshow('circle_img_'+str(minDist),img)       # 显示新图像
    cv2.waitKey(0)
cv2.destroyAllWindows()

