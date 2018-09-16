import requests
import time
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def main():

    # browser = webdriver.Chrome()
    # url = 'https://www.imooc.com'
    # wait = WebDriverWait(browser, 10)
    # browser.get(url)
    # signup_btn = wait.until(EC.presence_of_element_located((By.ID, 'js-signup-btn')))
    # signup_btn.click()
    # image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.verify-img')))
    # src = image.get_attribute('src')
    #
    # print(src)
    # print(signup_btn)
    # print(image)
    # print(browser.page_source)
    os.mkdir('result1')
    for i in range(100):
        url = 'https://www.imooc.com/passport/user/verifycode?t='
        url += str(int(round(time.time()*1000)))
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Referer':'https://www.imooc.com/',
            'Host':'www.imooc.com'
        }

        cookies = {
            'Cookie':'imooc_uuid=ffe6dc20-2dbc-4b80-ba9f-9721a59507df; imooc_isnew_ct=1511359153; imooc_isnew=2; Hm_lvt_fb538fdd5bd62072b6a984ddbc658a16=1536935432; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1536935432; PHPSESSID=cij8i17ohdemehikqm3s8l7br3; UM_distinctid=165d8912108ad-07299495956745-3961430f-100200-165d8912109456; IMCDNS=0; CNZZDATA1273767208=151572579-1536970614-https%253A%252F%252Fwww.imooc.com%252F%7C1536970614; CNZZDATA1273908995=1765438887-1536972206-https%253A%252F%252Fwww.imooc.com%252F%7C1536972206; Hm_lpvt_fb538fdd5bd62072b6a984ddbc658a16=1536972577; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1536972577; cvde=5b9bc601db4c4-25'
        }
        res = requests.get(url, headers=headers, cookies = cookies)
        # print(res.text)
        print(res.content)
        with open('result1//' + str(i) + '.jpg', 'wb') as f:
            f.write(res.content)
        # browser.close()


if __name__ == '__main__':
    main()