import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 8)


def main():
    headers = {
        'Accept': '*/*',
        'Cookie': 'BAIDUID=2176D64D05517AC3780B774A47F39EB6:FG=1; BIDUPSID=2176D64D05517AC3780B774A47F39EB6; PSTM=1539070163; BDUSS=1lsMWZKSFRUWjBzTDU0TjNJMWxCdnJmc0tOTUR4N2E2MDNxeGdINmZxSk5LdlZiQVFBQUFBJCQAAAAAAAAAAAEAAADi6c1PYmJveb-nt8jX0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE2dzVtNnc1bb; MCITY=-218%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_da3258e243c3132f66f0f3c247b48473=1541989917; H_PS_PSSID=26522_1446_21094_27400; delPer=0; PSINO=2',

        'Referer': 'https://zhaopin.baidu.com/quanzhi?query=%E7%94%B5%E5%B7%A5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
    url = 'https://zhaopin.baidu.com/api/qzasync?query=%E7%94%B5%E5%B7%A5&city=%25E6%25AD%25A6%25E6%25B1%2589&is_adq=1&pcmod=1&token=%3D%3DgxS36qXCe1VhYmV62ZYW2ZoxWZVR1ZbmZaYaZnqFJa&pn=0&rn=10'

    res = requests.get(url, headers=headers)
    print(res.status_code)
    data = res.json()
    print(res.text)

    for item in data['data']['disp_data']:
        print(item['@name'])

        detail_url = 'https://zhaopin.baidu.com/szzw?id=' + item['loc'] + '&query=%E7%94%B5%E5%B7%A5&city=%E6%AD%A6%E6%B1%89&is_promise=0&is_direct=&vip_'
        print(detail_url)

        try:

            browser.get(detail_url)
            more_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ' .job-description-more')))
            more_button.click()
            html = browser.page_source
            # print(html)
            soup = BeautifulSoup(html, 'html.parser')
            det_list = soup.select('.job-detail')

            detail_desc = soup.select('.job-desc-item')[0]
            class_list = detail_desc.select('.job-classfiy p')

            public_time = class_list[1].string
            useful_time = class_list[2].string
            print(public_time)
            print(useful_time)
            print(det_list)
        except Exception as e:
            print(e)

            continue


if __name__ =='__main__':
    main()
