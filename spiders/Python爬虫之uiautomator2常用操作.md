## uiautomator2常用操作

```python
import uiautomator2 as u2
import time
import traceback

if __name__ == '__main__':
    # 连接手机
    d = u2.connect("91AX1VNPG")
    appPackage = 'com.baidu.hi'
    appActivity = 'com.baidu.hi.activities.Logo'

    # 设置全局等待
    # d.settings['wait_timeout'] = 15

    # 清除app数据
    d.app_clear(appPackage)

    # 启动app应用（方式一）
    sess = d.session(appPackage)
    # 启动app应用（方式二）
    # d.app_start(appPackage, appActivity, wait=True)

    # 元素定位点击，如果没有设置全局等待时间，默认查找元素时间是20s,20s找不到会报错uiautomator2.exceptions.UiObjectNotFoundError
    d(resourceId="com.taobao.idlefish:id/right_btn").click()
    # 单独针对某个元素设置等待时间
    d(resourceId="com.taobao.idlefish:id/right_btn").click(timeout=10)

    # 输入手机号码
    d(resourceId="com.taobao.idlefish:id/aliuser_login_account_et").send_keys('17007123195')

    # 判断元素是否存在
    if d(resourceId="com.taobao.idlefish:id/aliuser_login_account_et").exists(timeout=3):
        print('找到手机号输入框')

    # 通过文本内容定位
    d(text="请输入淘宝账户").send_keys('123456')
    # 文本内容模糊定位
    d(textContains='忘记密').click()

    # 滑动认证，自动拖动，从左往右拖动到底
    d(resourceId="nc_1_n1t", index="0").drag_to(1039, 481, duration=2)

    # 向左滑动屏幕
    d.swipe_ext("left", scale=0.9)

    # 截图指定元素
    im = d(resourceId="com.iflytek.vflynote:id/tv_agree").screenshot()
    im.save("讯飞.jpg")

    # 捕捉toast
    msg = d.toast.get_message(5.0, 10.0, "")
    if '请输入验证码' in msg:
        print('出现图片验证码')
```
