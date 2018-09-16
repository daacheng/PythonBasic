import matplotlib.pyplot as plt
import matplotlib

# 垂直条形图
def main():
    # 统计数据
    data = {'东湖高新区': 21016.46,
            '洪山区': 19673.17,
            '江岸区': 24970.01,
            '东西湖区': 16142.81,
            '汉阳区': 19079.9,
            '武昌区': 27032.32,
            '江汉区': 21933.65,
            '硚口区': 19577.95,
            '黄陂区': 14796.93,
            '江夏区': 16194.93,
            '青山区': 20422.83,
            '蔡甸区': 13206.6,
            '新洲区': 7637.38,
            '汉南区': 9445.6,
            '沌口区': 15587.82}

    # 指定默认字体，可以支持中文
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'

    # 绘图
    # 第一个参数表示：每个柱x轴左边界，第二个参数表示：每个柱y轴下边界
    plt.bar(range(15), data.values(), width=0.5, align='center', color='steelblue', alpha=0.8)
    plt.title('武汉各地区二手房价格比较')
    # 轴标签
    plt.ylabel('价格')
    # 刻度标签
    plt.xticks(range(15), data.keys())
    # 设置Y轴范围
    plt.ylim([5000, 30000])
    # 为每个条形图添加数值标签
    for x, y in enumerate(data.values()):
        # 前两个参数表示标签的坐标位置，第三个参数表示标签的值
        plt.text(x, y+500, '%s' %round(y, 1), ha='center')
    plt.show()


if __name__ == '__main__':
    main()