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
