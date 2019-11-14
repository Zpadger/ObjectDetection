#加载模型

import numpy as np
from PIL import Image
from keras.models import load_model

load_model = load_model("mnist_model.h5")

###读取新的图片并转换为28*28的格式
im = Image.open("4.png")
im = im.convert("L")
im = im.resize((28, 28),Image.ANTIALIAS)
data = im.getdata()
data = np.array(data)
data = np.reshape(data,(28,28))
for i in range(len(data)):
    for j in range(len(data[0])):
        data[i][j] = 255 - data[i][j]

###转换为模型的输入维度
newimg = data.reshape(1,28,28,1)
###识别图片数字
predict = load_model.predict(newimg)
predict = np.argmax(predict)
print('predicted:', predict)