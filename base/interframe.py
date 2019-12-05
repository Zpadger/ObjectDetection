#帧间差分法
import cv2

filename="/home/zpj/桌面/out2.mp4" #视频文件输入
camera=cv2.VideoCapture(filename)

#视频文件输出参数设置
out_fps=12.0 #输出文件帧率
fourcc=cv2.VideoWriter_fourcc('M','P',"4",'2')
out1=cv2.VideoWriter('/home/zpj/桌面/v1.avi',fourcc,out_fps,(500,400))
out2=cv2.VideoWriter('/home/zpj/桌面/v2.avi',fourcc,out_fps,(500,400))

#初始化当前帧的前一帧
lastFrame=None

#遍历视频的每一帧
while camera.isOpened():

    #读取下一帧
    (ret,frame)=camera.read()

    #如果不能抓取到每一帧，说明已经到达视频的结尾
    if not ret:
        break

    #调整该帧的大小
    frame=cv2.resize(frame,(500,400),interpolation=cv2.INTER_CUBIC)

    #如果第一帧是None，对其初始化
    if lastFrame is None:
        lastFrame=frame
        continue

    #计算当前帧与前一帧的不同
    frameDelta=cv2.absdiff(lastFrame,frame)

    #当前帧设置为下一帧的前一帧
    lastFrame=frame.copy()

    #结果转变为灰度图
    thresh=cv2.cvtColor(frameDelta,cv2.COLOR_BGR2GRAY)

    #图像二值化处理
    thresh=cv2.threshold(thresh,25,255,cv2.THRESH_BINARY)[1]

    cnts,hierarchy=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #ValueError: not enough values to unpack (expected 3, got 2)————删除binary变量

    for c in cnts:
        if cv2.contourArea(c)<300:
            continue

        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("frame",frame)
    cv2.imshow("frameDelta",frameDelta)
    cv2.imshow("thresh",thresh)

    out1.write(frame)
    out2.write(frameDelta)

    if cv2.waitKey(200)&0xFF==ord('q'):
        break

out1.release()
out2.release()
camera.release()
cv2.destroyAllWindows()
