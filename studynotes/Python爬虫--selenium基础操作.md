# Python爬虫--selenium基础操作
## selenium访问页面

    from selenium import webdriver
    import time

    # selenium访问页面
    # 创建浏览器对象
    browser = webdriver.Chrome()
    # 发起请求
    browser.get('https://www.baidu.com')
    # 获取返回结果
    print(browser.current_url)
    print(browser.page_source)
    time.sleep(3)
    # 关闭浏览器
    browser.close()
    
## selenium节点查找

    from selenium import webdriver
    import time

    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    # 单个节点查找
    # 通过id查找
    input_first = browser.find_element_by_id('q')
    # 通过css选择器查找
    input_second = browser.find_element_by_css_selector('#q')
    # 通过xpath语法查找
    input_third = browser.find_element_by_xpath('//*[@id="q"]')

    # <selenium.webdriver.remote.webelement.WebElement (session="7f8bd32998092a56e76ca6b7962c0446", element="0.7915941665437694-1")>
    print(input_first)
    print(input_second)
    print(input_third)

    # 多个节点查找
    li_1 = browser.find_elements_by_xpath('//li[contains(@class,"J_Cat")]')
    li_2 = browser.find_elements_by_css_selector('.service-bd li')
    print(li_1)
    print(li_2)

    time.sleep(5)
    browser.close()

## 节点交互

    from selenium import webdriver
    import time

    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')

    # 节点交互

    # 找到input输入框
    input_first = browser.find_element_by_id('q')
    # 输入要查询的关键字
    input_first.send_keys('小米')
    time.sleep(1)
    # 清空输入框
    input_first.clear()
    input_first.send_keys('华为')
    # 找到查询按钮
    button = browser.find_element_by_class_name('btn-search')
    # 点击查询
    button.click()
    time.sleep(5)
    browser.close()
## 获取节点属性值

    from selenium import webdriver
    import time

    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    logo = browser.find_element_by_id('zh-top-link-logo')
    print(logo)

    # 获取节点属性值
    print(logo.get_attribute('class'))
    print(logo.get_attribute('href'))

    btn = browser.find_element_by_class_name('zu-top-search-button')
    # 获取文本值
    print(btn.text)

    time.sleep(5)
    browser.close()
## 延时等待
使用selenium去请求网页获取资源的时候，可能会有些ajax请求资源还没有返回，这时候需要等待一段时间，等待页面完全加载。
### 隐式等待
使用隐式等待，如果浏览器没有找到DOM节点，会等待一段时间，再去查找节点，超出时间会抛出异常。

    from selenium import webdriver

    browser = webdriver.Chrome()
    # 隐式等待
    browser.implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    logo = browser.find_element_by_id('zh-top-link-logo')
    print(logo)
    browser.close()

### 显式等待

    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC

    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    # 创建一个wait对象,指定最长等待时间是10秒
    wait = WebDriverWait(browser,10)
    # expected_conditions  EC是指的等待的条件对象
    # presence_of_element_located 指等待指定节点加载出来
    # element_to_be_clickable 指等待节点可点击
    in_put = wait.until(EC.presence_of_element_located((By.ID,'q')))
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))

    print(in_put.tag_name)   # input
    print(btn.tag_name)   # button
    browser.close()
