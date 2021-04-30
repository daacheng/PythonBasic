# opencv-python基础
* pip install opencv-python

## 1.图像的读取、显示、保存
```python
import cv2

if __name__ == '__main__':

    # 1:加载彩色图像 0:灰度模式 -1:加载图像，包括alpha通道
    img = cv2.imread("test.jpg", -1)
    cv2.namedWindow('window1', cv2.WINDOW_NORMAL)  # 创建一个默认大小的窗口
    cv2.imshow('window1', img)  # 窗口显示图像
    key_event = cv2.waitKey(0)  # 键盘绑定，点击键盘程序继续执行
    if key_event == 27:
        # ESC按键
        cv2.destroyAllWindows()  # 关闭所有窗口
    elif key_event == ord('s'):
        # 按键s
        cv2.imwrite('new_test.jpg', img)  # 写图片
        cv2.destroyAllWindows()
```

## 2.绘制直线、圆、矩形、多边形，文本
```python
import cv2
import numpy as np


if __name__ == '__main__':
    # 创建一个高512，宽512的黑色图片
    img = np.zeros((512, 512, 3), np.uint8)
    # 从左上角到右下角画一条直线，厚度为5像素，蓝色(255, 0, 0)
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

    # 画矩形,指定矩形的左上角和右下角，绿色(0, 255, 0)
    cv2.rectangle(img, (300, 0), (500, 100), (0, 255, 0), 3)

    # 画一个圆，指定圆心和半径,红色(0, 0, 255)
    cv2.circle(img, (300, 100), 150, (0, 0, 255), 3)

    # 画一个椭圆
    cv2.ellipse(img, (300, 100), (100, 50), 0, 0, 180, 255, -1)

    # 画多边形,首先需要顶点的坐标,将这些点组成形状为rowsx1x2的数组，其中rows是顶点数，并且其类型应为int32。
    pts = np.array([[10, 10], [100, 10], [100, 150], [10, 200]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    # True是闭合的折线，False不闭合
    cv2.polylines(img, [pts], False, (0, 255, 255))

    # 添加文本,指定文本内容，左下角坐标，字体，大小，颜色，厚度，线性
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, '123321123ddd', (0, 500), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('window1', img)
    key_event = cv2.waitKey(0)
    cv2.destroyAllWindows()
```

## 3.访问修改像素值
```python
import time
import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('roi.jpg')
    # 通过行列坐标访问像素，BGR图像返回一个[蓝色，绿色，红色值]的数组，灰度图像仅返回相应的强度
    px = img[100, 100]
    print(px)
    # 修改像素
    img[100, 100] = [255, 255, 255]
    print(img[100, 100])
    # 图像的形状,数据类型
    print(img.shape, img.dtype)

    # 替换指定区域图像
    ball = img[220:280, 270:330]
    img[100:160, 100:160] = ball

    # 分割合并图像通道，一般用numpy索引 或者：b = img[:, :, 0]
    b, g, r = cv2.split(img)
    img = cv2.merge((b, g, r))

    cv2.imshow('window1', img)
    key_event = cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 将红色通道全部设置为0
    img[:, :, 2] = 0

    cv2.imshow('window1', img)  # 窗口显示图像
    key_event = cv2.waitKey(0)
    cv2.destroyAllWindows()
```
