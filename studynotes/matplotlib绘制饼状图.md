# matplotlib绘制饼状图
学习from：https://www.kesci.com/home/project/59f6de30c5f3f511952c1211

    % matplotlib inline
    import matplotlib
    import matplotlib.pyplot as plt

    # 构造数据
    data = [0.4,0.3,0.1,0.2]
    labels = ['音乐','舞蹈','编程','数学']
    explode = [0,0.1,0,0]  # 用于突出圆饼图指定的一块数据，这里突出‘舞蹈’这部分
    colors=['#9999ff','#ff9999','#7777aa','#2442aa','#dd5555'] # 自定义颜色

    #指定默认字体，可以支持中文
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family']='sans-serif'


    #  plt.pie(x=data,    绘图数据来源
    #       labels=labels, 添加标签
    #       explode=explode,  突出显示哪一部分内容
    #       colors=colors,    设置饼图填充颜色
    #       autopct='%.1f%%', 设置百分比的格式，这里保留一位小数
    #       pctdistance=0.6,   百分比标签与圆心的距离
    #       labeldistance = 1.1,  文字标签与圆心的
    #       radius = 2,   半径大小
    #       wedgeprops = {'linewidth': 2, 'edgecolor':'pink'}, 设置边界属性
    #       textprops = {'fontsize':12, 'color':'k'},center = (0.2,0.2))   设置字体属性

    # 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
    plt.axes(aspect='equal')
    plt.pie(x=data,
            labels=labels,
            explode=explode,
            colors=colors,
            autopct='%.1f%%',
            pctdistance=0.6,
            labeldistance = 1.1,
            radius = 2,
            wedgeprops = {'linewidth': 2, 'edgecolor':'pink'},
            textprops = {'fontsize':19 ,'color':'k'},
            center = (0.2,0.2))
    plt.title('圆饼图')
    plt.show()

![](https://github.com/daacheng/PythonBasic/blob/master/pic/pie.png)
