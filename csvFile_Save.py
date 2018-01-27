import requests, csv
from bs4 import BeautifulSoup

res = requests.get('http://www.jxyycg.cn/yzxt/publicity/view?id=eb1a21f2ab6a40119544e9048417bc1f&pageNo=1')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
table_body = soup.select('.hover')

# table_body=soup.find_all('tr',{'class':'hover'})
# for tr in table_body:
#     print(tr.select('td'))
#    for td in tr.select('td'):
#        print(td.text)
#    print('------------------------')

for tr in table_body:
    # print(tr.select('td'))
    content = [td.text for td in tr.select('td')]
    print(content)
    # print(content)

    # ‘a’模式表示打开一个文件用于追加。
    # 如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。
    # 如果该文件不存在，创建新文件进行写入。
    with open('csv_save.csv', 'a', newline='') as f:  # 删除空格
        f_csv = csv.writer(f)
        f_csv.writerow(content)
        f.close()

