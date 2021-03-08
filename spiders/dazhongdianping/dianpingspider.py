from fake_useragent import UserAgent
import requests
ua = UserAgent()


def main():
    url = 'http://www.dianping.com/shop/113152394/review_all/p2'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cookie': 'cy=16; cye=wuhan; _lxsdk_cuid=166fd58c269c8-0ce4a20f80c75d-36664c08-100200-166fd58c26ac8; _lxsdk=166fd58c269c8-0ce4a20f80c75d-36664c08-100200-166fd58c26ac8; _hc.v=25914a1f-3eb2-f2fe-0a2a-5dab25f41628.1541848745; thirdtoken=EB9A92578C9AD27BD84DD3EB924C3D96; JSESSIONID=19DB1130821C481CCD3726CE65ED33DA; _thirdu.c=59ead4a561a2f8759354d4a000bf3977; dper=f2c7f32d6dcc02ee0477bab8efa7bfd02a44674cfba36e9a3312837a4bdbc9b7768935e70e67c6c01e1a25596ddb8ea43858514a9d918c54f3258720154ee2db738e5f0fad922e38cb495a8a0e3e4f8257f070773defcb02ad1c60d6c9744be8; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_5215652574; ctu=f6877174f2e8dca3a95dd02be3844a396f58c7d5f9ab55868b4a60c460b10f80; uamo=18571510652; s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16700cdead0-3c6-cf9-1dd%7C%7C281',
        'Referer': 'http://www.dianping.com/shop/113152394/review_all',
    }

    res = requests.get(url, headers=headers)
    print(res.status_code)
    print(res.text)
    with open('1.html', 'w', encoding='utf-8') as f:
        f.write(res.text)

if __name__ == '__main__':

    main()