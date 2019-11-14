#使用训练好的模型识别数字

import numpy as np
from keras.models import load_model
from PIL import Image

load_model = load_model("mnist_model.h5")

###定义函数识别数字
def returnnum(im):

    data = np.reshape(im,(28,28))
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = 255 - data[i][j]

    ###转换为模型的输入维度
    newimg = data.reshape(1,28,28,1)

    ###识别图片数字
    predict = load_model.predict(newimg)
    predict = np.argmax(predict)

    return predict

###读取图像并处理
num = 3    ##数字个数
img = Image.open("187.png")
img = img.convert("L")
img = img.resize((28*num, 28),Image.ANTIALIAS)
imgdata = np.array(img)

steps = 28 ##每个数字图像宽度
newm = []
for i in range(num):
    if i == num-1:
        newdata = imgdata[:,i*steps:]
        prenum = returnnum(newdata)
        newm.append(prenum)
    else:
        newdata = imgdata[:,i*steps:(i+1)*steps]
        prenum = returnnum(newdata)
        newm.append(prenum)

###输出图像中的数字
print(newm)