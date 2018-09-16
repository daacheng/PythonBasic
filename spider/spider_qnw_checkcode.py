from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
import os


def main():
    os.mkdir('result')
    for i in range(100):
        url = 'https://user.qunar.com/captcha/api/image?k={en7mni(z&p=ucenter_login&c=ef7d278eca6d25aa6aec7272d57f0a9a&t='
        ms = str(int(round(time.time()*1000)))
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
        }
        res = requests.get(url+ms, headers=headers)
        print(res.content)
        with open('result//' + ms + '.jpg', 'wb') as f:
            f.write(res.content)


if __name__ == '__main__':
    main()