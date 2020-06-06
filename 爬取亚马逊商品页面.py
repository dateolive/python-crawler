import requests
def httpymxtext(url):
    try:
        kv={
            'user-agent':'Mozilla/5.0',
            'cookie':' _uuid=47D3DAF9-F93B-BB54-DF0E-50FA495DDDB748997infoc; buvid3=63638A1C-180D-4606-B086-8F7511E66146155815infoc; sid=82e6c56u; DedeUserID=100669401; DedeUserID__ckMd5=048124831d1f5a4c; SESSDATA=102644af%2C1603697285%2C6eb1b*41; bili_jct=9869499338e5484369029eccfaddf32f',
            }
        r=requests.get(url,headers=kv)#通过headers模拟浏览器爬取信息
        r.raise_for_status()
        print('111')
        print(r.status_code)
        r.encoding=r.apparent_encoding
        return (r.text[1000:2000])
    except:

        print("爬取失败")
if __name__=="__main__":
    url=input()
    print(httpymxtext(url))
