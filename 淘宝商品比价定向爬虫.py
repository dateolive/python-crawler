import requests
import re
def gethttptext(url):
    try:
        kv = {
            'cookie':'Here is the cookie after logging in with your Taobao account',
            'user-agent':'Mozilla/5.0'
        }
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("提取失败")
        return ""

def parsepage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        # print(tlt)
        print(len(plt))
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([title, price])
        # print(ilist)
    except:
        print("解析出错")

def printgoodslist(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))

if __name__=="__main__":
    goods='玫瑰花'
    depth=2
    start_url='https://s.taobao.com/search?q='+goods
    infolist=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=gethttptext(url)
            parsepage(infolist,html)
        except:
            continue
    printgoodslist(infolist)




