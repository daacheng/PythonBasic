import requests

session = requests.session()
def main():
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"

    header = {
        "HOST": "www.zhihu.com",
        "Referer": "https://www.zhihu.com/",
        "User-Agent": agent,
    }
    res = session.post("https://www.zhihu.com/signup?next=%2F", headers=header)
    print(res.cookies['_xsrf'])


if __name__ == '__main__':
    main()