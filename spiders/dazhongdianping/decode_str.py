import re
import requests
from lxml import etree
import json
from lxml import etree
from fake_useragent import UserAgent

ua = UserAgent()

def main():
    #得到css样式
    # url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/shoptextcss/textcss.hHGEFeGyJG.css'

    url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/73935aee5f33d2bd52d6b427cddaaa09.css'
    res = requests.get(url=url)
    # print(res.text)

    # 每个类.sj-tuDm 对应一个点位  '.sj-tuDm{background:-126.0px -427.0px;}'
    pattern = re.compile(r'.sj-.*?}')
    class_items = pattern.findall(res.text)
    print(class_items)

    # 获取编码表的url
    pattern = re.compile(r'//.*.svg')
    file_svg = pattern.findall(res.text)
    print(file_svg)

    # 获取编码表内容
    svg_url = 'http:' + file_svg[0]
    decode_html_str = requests.get(svg_url).text
    line_pattern = re.compile(r'class="textStyle">(.*?)</text>')
    lines = line_pattern.findall(decode_html_str)
    with open('decode_str.txt', 'a', encoding='utf-8') as fp:
        fp.write(''.join(lines))
    print(''.join(lines))

    # 三、生成标识和汉字编码表的对照关系
    word_dic = {}
    # 每个类 .sj-tuDm 对应一个汉字
    for item in class_items:
        print(item)
        if 'sj-"]' in item:
            continue
        # 字宽14，高30  margin-top: -9px
        # 获取每个类对应的x位置，y位置
        locaton_x = re.compile('background:(.*?)px')
        x_list = locaton_x.findall(item)

        locaton_y = re.compile('px (.*?)px')
        y_list = locaton_y.findall(item)

        x = abs(float(x_list[0]))
        y = abs(float(y_list[0]))

        print(item[:8], 'loc:(', x, ',', y, ')')
        # 行、列变为一行读取
        #         x   y  index
        # 第一行：0   7    0
        # 第二行：0   37   42
        x_0 = int(x / 14)  # 表示第几列
        y_0 = int(y) // 30  # 表示第几行
        print('index:', x_0, '列', y_0, '行')
        #                 行  行中第n个字
        word = lines[y_0][x_0:x_0 + 1]
        print(item[:8], word)

        # 添加到字典当中
        k = item[1:8]
        word_dic[k] = word

    # 读取原始网页资源
    content = ''
    with open('1.html', 'r', encoding='utf-8') as fp:
        content = fp.read()

    # 获取所有的span标签 <span class="sj-ljyv"></span>
    pattern = re.compile(r'<span class="sj-.*?"></span>')
    span_list = pattern.findall(content)
    print(span_list)

    for span_str in span_list:
        # 获取每一个span标签中的class属性值
        pattern = re.compile(r'sj-\S{4}')
        span_class = pattern.findall(span_str)

        value_of_span_class = ''  # 替换后的文字
        if span_class:
            # 通过编码关系字典，找到每个class对应的文字，然后把span标签替换成文字
            value_of_span_class = word_dic.get(span_class[0], '')
            print(span_str, '--->', value_of_span_class)
            content = content.replace(span_str, value_of_span_class)

    print(content)

    with open('2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    html = etree.HTML(content.replace('<br>', ''))
    reviews = html.xpath('//div[@class="main-review"]/div[contains(@class,"review-words")]')
    print(reviews)
    for review in reviews:
        print(review.xpath('string(.)').replace(' ', '').replace('\n', ''))
        # print(review.replace(' ', '').replace('\\n', ''))
        print('=====================================================')


if __name__ == '__main__':

    main()