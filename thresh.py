import numpy as np
import cv2

img=cv2.imread('answer_sheet.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,gray=cv2.threshold(gray,90,255,cv2.THRESH_BINARY_INV)

gray=cv2.erode(gray,None)
gray=cv2.dilate(gray,None)

contours,hierarchy=cv2.findContours(gray.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
newing=np.zeros_like(gray)
cv2.drawContours(newing,contours,-1,255)
cv2.imshow('test',newing)
cv2.imwrite("processed.jpg",newing)
cv2.waitKey()