import requests
import csv
import time


def main():
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'BAIDUID=F06807DA7912693A50762BACBC263B18:FG=1; BIDUPSID=F06807DA7912693A50762BACBC263B18; PSTM=1509429742; BDUSS=0V5RXE5aEhrYzBiblZvazJ3TTl5MGc1TTJuclF-VjVwS0pvUWlkaFpSU05JU1JhSVFBQUFBJCQAAAAAAAAAAAEAAADi6c1PYmJveb-nt8jX0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI2U~FmNlPxZN; MCITY=-269%3A218%3A; __cfduid=d88b8fe30afaab904744fce685e5e00771514706576; Hm_lvt_c676f95eebbd4fa8a59418f48090ac4d=1532250572; Hm_lvt_4b55f5db1b521481b884efb1078a89cc=1541936973; Hm_lvt_da3258e243c3132f66f0f3c247b48473=1541936494,1542031111; Hm_lpvt_da3258e243c3132f66f0f3c247b48473=1542031111',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Referer': 'http://zhaopin.baidu.com/quanzhi?query=%E6%B0%B4%E7%94%B5%E5%B7%A5'
    }

    with open('query_condition.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            print(row)
            token = '%3D%3DAlj2KpD%2F90XRlaW%2BWmqZWattGZTl1mopman1Jlqpml'
            # url = 'http://zhaopin.baidu.com/api/qzasync?query=%s&city=%s&is_adq=1&pcmod=1&token=%s&pn=10&rn=10&date=%s_%s' % ('%E6%B0%B4%E7%94%B5%E5%B7%A5', '%25E6%25AD%25A6%25E6%25B1%2589', token, row[3], row[4])

            url = 'http://zhaopin.baidu.com/api/qzasync?query=%E6%B0%B4%E7%94%B5%E5%B7%A5&city=%25E6%25AD%25A6%25E6%25B1%2589&is_adq=1&pcmod=1&token=%3D%3DAlj2KpD%2F90XRlaW%2BWmqZWattGZTl1mopman1Jlqpml&pn=10&rn=10&date=20181111_20181112'
            print(url)
            res = requests.get(url, headers=headers)
            print(res.text)
            time.sleep(10)


if __name__ == '__main__':
    data = '%E6%B0%B4%E7%94%B5%E5%B7%A5'

    main()