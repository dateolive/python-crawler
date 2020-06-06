import requests
import re
def gethttptext(url):
    try:
        kv = {
            'cookie':'mt=ci%3D-1_0; t=c0f14c167c6f77b42f232b5d9863d4c4; cna=XjwfFx4NvH4CAXFADDy7a4Iu; UM_distinctid=172356aa9de2be-0e2f98008506be-d373666-144000-172356aa9df269; thw=cn; tfstk=cfilB3azJ4zW6C3SCTZSKRARgQ-OZGLzNDoq00NqPiGYgWnVih_V7EmDn7hovw1..; sgcookie=EHjFUQcuITbexzaIoNAlV; uc3=id2=UNN%2F78ANp1Cw1A%3D%3D&nk2=qTwX93t8BoncWg%3D%3D&vt3=F8dBxGZs8fd2j9dAk54%3D&lg2=UIHiLt3xD8xYTw%3D%3D; lgc=%5Cu5341%5Cu9999%5Cu91711314; uc4=nk4=0%40q3nO8Q%2BRMegduVuLtMgbHVjnKme2&id4=0%40UgQ3ABDRxpGA4bhBiFQR4rS3tgVP; tracknick=%5Cu5341%5Cu9999%5Cu91711314; _cc_=UtASsssmfA%3D%3D; enc=105nsbE7EjzJWtfy19a1BMVBzFpipu6TPRPD1Xt4qAM%2BATQRZ4jNf%2FGgtTAfUgOAJP5qgdarimwjwQOD%2BwTXbQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; v=0; cookie2=1e4dead55b98aeee792c389067aecebd; _tb_token_=e5e915537a178; _nk_=%5Cu5341%5Cu9999%5Cu91711314; JSESSIONID=2E121E1A82682CDABB77C7D2DA7B94A4; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; mt=ci=-1_0; uc1=cookie14=UoTV7Nd3d%2FjPeg%3D%3D; l=eBNQAmqPQlfeDgSbBOfwnurza77tIIRAguPzaNbMiOCPOgCp5CRfWZAkKlT9CnGVh6f2R3ykIQI6BeYBqIv4n5U62j-lasHmn; isg=BLm5VfRRw28fjp-H6cxGHI9WyCWTxq14vTZiitvuM-BfYtn0IxSGSbGw4GaUWkWw',
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




