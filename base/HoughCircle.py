#霍夫变换检测圆形
import cv2
import numpy as np


def detect_circle_demo(image):
    # dst = cv2.bilateralFilter(src=image, d=0, sigmaColor=100, sigmaSpace=5) # 高斯双边滤波(慢)
    dst = cv2.pyrMeanShiftFiltering(image, 10, 100)                           # 均值偏移滤波（稍微快）
    dst = cv2.cvtColor(dst, cv2.COLOR_BGRA2GRAY)

    cv2.imshow("adapt_image", dst)
    circle = cv2.HoughCircles(dst, cv2.HOUGH_GRADIENT, 1, 200, param1=50, param2=30, minRadius=50, maxRadius=300)
    if not circle is None:
        circle = np.uint16(np.around(circle))
        print(circle)
        for i in circle[0, :]:
            cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 1)
            cv2.imshow("circle", image)


if __name__ == "__main__":
    src = cv2.imread("footbals.jpg")
    src = cv2.resize(src, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

    detect_circle_demo(src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
