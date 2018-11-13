from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options = chrome_options)
wait = WebDriverWait(browser, 15)


def main():
    # 要爬取的url
    city = '武汉'
    job = '水电工'
    url = 'https://zhaopin.baidu.com/quanzhi?city='+ city +'&query=' + job
    print(url)
    browser.get(url)
    print(browser.page_source)


if __name__ == '__main__':
    main()