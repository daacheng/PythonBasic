## 1.基础操作

```python
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # 谷歌浏览器驱动
    chromedriver_path = 'chromedriver72.exe'
    options = webdriver.ChromeOptions()
    # 躲避部分网站selenium检测
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    # 躲避部分网站selenium检测
    script = "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})

    # 浏览器最大化
    driver.maximize_window()

    url = 'https://www.python.org/'
    driver.get(url)
    # 显式等待
    wait = WebDriverWait(driver, 20, 1)

    # 在主页输入框搜索requests，并点击搜索
    input_ = wait.until(EC.presence_of_element_located((By.ID, 'id-search-field')))
    input_.send_keys('requests')
    time.sleep(1)
    btn = driver.find_element_by_xpath('//button[@title="Submit this Search"]')
    btn.click()
    time.sleep(10)
    driver.close()
```

## 2.元素定位
#### 查找单个元素
最常用的定位元素的两个方法是通过Xpath和id来定位。
* find_element_by_id
* find_element_by_xpath

#### 查找多个元素
* find_elements_by_xpath
* find_elements_by_name

```python
# 通过xpath查找元素
driver.find_element_by_xpath('//button[@title="Submit this Search"]')
# 通过id查找元素
driver.find_element_by_id('id-search-field')
```
#### 获取元素内部内容
```python
text = driver.find_element_by_xpath('//*[@id="ISDCaptcha"]/div[2]/div').get_attribute('innerHTML')
if '请绘制图中手势' in text:
    print('出现行为认证')
```
#### 获取元素指定属性的属性值
```python
driver.find_element_by_xpath('//div[@id="find-step3-phone"]').get_attribute('style')
driver.find_element_by_xpath('//*[@id="imgVerifyCodeP"]').get_attribute('src')
```
#### 切换到指定iframe
```python
# 通过id或者名称
driver.switch_to.frame("iframeLoginIfm")

browser.switch_to.frame(0)

frame = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
driver.switch_to.frame(frame)
```
#### 切换到指定窗口
```python
driver.switch_to.window(browser.window_handles[1])
```
#### 切换到alert弹窗
```python
text = driver.switch_to.alert.text
if '图片验证码输入错误' in text:
    print('图片验证码识别错误')
    driver.switch_to.alert.accept()
```

## 3.元素交互
#### 按钮点击
```python
btn = driver.find_element_by_xpath('//div[@role="button"]/div/span/span')
btn.click()
```
#### 执行js代码
```python
style_ = driver.find_element_by_xpath('//*[@id="passport-login-pop"]').get_attribute('style')
style_ = style_.replace('display: none;', '')
if not style_:
    style_ = 'left: 259px; top: 212px; z-index: 60001;'
js = 'document.getElementById("passport-login-pop").setAttribute("style","{}");'.format(style_)
driver.execute_script(js)
```

#### 表单输入
```python
input_ = driver.find_element_by_xpath('//input[@name="session[password]" and @dir="auto"]')
input_.send_keys('123qwe')

from selenium.webdriver.common.keys import Keys
input_.send_keys(Keys.BACK_SPACE)
```
#### 页面滚动
```python
driver.execute_script("""
                (function () {
                    var y = document.body.scrollTop;
                    var step = 100;
                    window.scroll(0, y);
                    function f() {
                        if (y < document.body.scrollHeight) {
                            y += step;
                            window.scroll(0, y);
                            setTimeout(f, 50);
                        }
                        else {
                            window.scroll(0, y);
                            document.title += "scroll-done";
                        }
                    }
                    setTimeout(f, 1000);
                })();
                """)
```
#### 模拟拖动
```python
from selenium.webdriver.common.action_chains import ActionChains

def get_track(self, distance):
    track = []
    current = 0
    mid = distance * 3 / 4
    t = 0.2
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track

# 模拟拖动
btn = wait.until(EC.presence_of_element_located((By.XPATH, xpath_)))
track = get_track(500)
action = ActionChains(browser)
action.click_and_hold(btn).perform()
action.reset_actions()
for i in track:
    action.move_by_offset(xoffset=i, yoffset=0).perform()
    action.reset_actions()
```

## 4.等待
#### 显式等待
```python
# 显式等待
wait = WebDriverWait(driver, 20, 1)

input_ = wait.until(EC.presence_of_element_located((By.ID, 'id-search-field')))
input_.send_keys('requests')
time.sleep(1)
```
#### 隐式等待
```python
from selenium import webdriver

browser = webdriver.Chrome()
# 隐式等待
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
browser.close()
```

## 5.其他操作
#### 解决页面加载时间过长问题
有时候页面有些静态文件加载比较耗时，selenium可以不需要等待页面全部加载完全在去查找元素
```python
options = webdriver.ChromeOptions()
# 解决页面加载阻塞问题
options.set_capability('pageLoadStrategy', 'none')
driver = webdriver.Chrome(executable_path=self.chromedriver_path, options=options)
```
#### 添加请求头
```python
options.add_argument("user-agent={}".format('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'))
```
#### 添加代理
```python
socks5 = "socks5://{}:{}".format(socks5_proxy_ip, socks5_proxy_port)
options.add_argument("--proxy-server={}".format(socks5))
```
#### 捕捉F12控制台中所有请求记录
```python
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

d = DesiredCapabilities.CHROME
d['loggingPrefs'] = {'performance': 'ALL'}
d['goog:chromeOptions'] = {
    'perfLoggingPrefs': {
        'enableNetwork': True,
    },
    'w3c': False,
}
options.add_experimental_option('perfLoggingPrefs', {'enableNetwork': True})
options.add_experimental_option('w3c', False)
driver = webdriver.Chrome(executable_path=self.chromedriver_path, options=options, desired_capabilities=d)

# 保存log
log_list = []
for entry in driver.get_log('performance'):
    log_list.append(entry)
```
#### 屏幕截图,可以截取图片验证码加以识别
```python
import win32con
import win32gui
import win32print
from win32api import GetSystemMetrics
from PIL import Image

def get_real_resolution():
    """获取真实的分辨率"""
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h

def get_screen_size():
    """获取缩放后的分辨率"""
    w = GetSystemMetrics(0)
    h = GetSystemMetrics(1)
    return w, h

real_resolution = get_real_resolution()
screen_size = get_screen_size()
screen_scale_rate = round(real_resolution[0] / screen_size[0], 2)

pic_name = '***.png'
driver.save_screenshot(pic_name)
# 找到图片验证码元素
element = driver.find_element_by_xpath(xpath_)
left = element.location['x'] * screen_scale_rate
top = element.location['y'] * screen_scale_rate
right = (element.location['x'] + element.size['width']) * screen_scale_rate
bottom = (element.location['y'] + element.size['height']) * screen_scale_rate
im = Image.open(pic_name)
# 裁剪图片
im = im.crop((left, top, right, bottom))
im.save(pic_name)
# 把图片转成base64,利用打码平台接口识别
with open(pic_name, 'rb') as f:
    code_img_base64 = base64.b64encode(f.read()).decode()
os.remove(pic_name)
```
