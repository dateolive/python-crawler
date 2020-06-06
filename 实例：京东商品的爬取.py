import requests
def httpjdtext(url):
    try:
        r=requests.get(url)
        r.raise_for_status()#如果状态不是200，则报错
        r.encoding=r.apparent_encoding
        return (r.text[:1000])
    except:
        print("爬取失败")
if __name__=="__main__":
    url=input()
    print(httpjdtext(url))
