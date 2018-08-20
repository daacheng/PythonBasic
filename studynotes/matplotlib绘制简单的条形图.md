## 垂直条形图

    % matplotlib inline
    import matplotlib.pyplot as plt

    # 垂直条形图
    # 构建数据
    GDP = [9386.7, 12406.5, 13908.6, 9000.94]

    # 绘图
    plt.bar(range(4),GDP, align='center', color='steelblue',alpha=0.8)
    plt.title('GDP')
    # 轴标签
    plt.ylabel('GDP')
    # 刻度标签
    plt.xticks(range(4),['chongqi','beijing','shanghai','wuhan'])
    # 设置Y轴范围
    plt.ylim([5000,15000])

    #为每个条形图添加数值标签
    for x,y in enumerate(GDP):
        # 前两个参数表示标签的坐标位置，第三个参数表示标签的值
    #     plt.text(x,y+200,y,ha='center')
        plt.text(x,y+200,'%s' %round(y,1),ha='center')
    plt.show()

![](https://github.com/daacheng/PythonBasic/blob/master/pic/vtiao.jpg)
## 水平条形图

    % matplotlib inline
    import matplotlib.pyplot as plt

    # 水平条形图
    price = [18.5,22.6,35,42.3,27.8]
    # 绘图
    plt.barh(range(5),price, align='center', color='steelblue',alpha=0.8)
    plt.title('price compaire')
    # 轴标签
    plt.xlabel('price')
    # 刻度标签
    plt.yticks(range(5),['a','b','c','d','e'])
    # 设置X轴范围
    plt.xlim([15,50])
    # 为每个条形图添加数值标签
    for x,y in enumerate(price):
        plt.text(y+1,x,y,va='center')
    plt.show()

![](https://github.com/daacheng/PythonBasic/blob/master/pic/htiao.jpg)
## 交错条形图

    % matplotlib inline
    import matplotlib.pyplot as plt
    import numpy as np

    # 构建数据
    Y2016 = [15600,12700,11300,4270,3620]
    Y2017 = [17400,14800,12000,5200,4020]
    labels = ['beijing','shanghai','xianggang','shenzhen','guangzhou']
    bar_width = 0.35
    # 绘图
    plt.bar(np.arange(5),Y2016, align='center', color='steelblue',alpha=0.8,width = bar_width)
    plt.bar(np.arange(5)+bar_width,Y2017, align='center', color='indianred',alpha=0.8,width = bar_width)
    plt.title('rich home')
    # 轴标签
    plt.xlabel('top citys')
    plt.ylabel('family nums')

    # 刻度标签
    plt.xticks(np.arange(5)+bar_width,labels)
    # y轴范围
    plt.ylim([2500,20000])

    for x,y in enumerate(Y2016):
        plt.text(x,y+200,y,ha='center')
    for x,y in enumerate(Y2017):
        plt.text(x+bar_width,y+200,y,ha='center')
    plt.show()

![](https://github.com/daacheng/PythonBasic/blob/master/pic/jiaocuotiao.jpg)
