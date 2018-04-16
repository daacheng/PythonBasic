from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
from pymongo import MongoClient

#定义数据库连接并将抓取到的商品数据保存到MongoDB中
client = MongoClient('localhost',27017)
taobao = client.taobao
collection_product = taobao.product

def save_to_mongodb(product): 
    try:
        if collection_product.insert(product):
            print('successful')
    except Exception:
        print('faile')



def getProducts():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('data-src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            'title':item.find('.title').text(),
            'location':item.find('.location').text(),
            'shop':item.find('.shop').text()
        }
        print(product)
        save_to_mongodb(product)

def index_page(page):
    print(page)
    try:
        browser.get(url)
        if page>1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(3)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        getProducts()
    except Exception:
        print('超时')

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
    
url = 'https://s.taobao.com/search?q=ipad'
for page in range(2,5):
    print(page)
    try:
        browser.get(url)
        if page>1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        getProducts()
    except Exception:
        print('超时')
