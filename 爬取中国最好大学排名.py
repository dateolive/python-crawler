import requests
import bs4
from bs4 import BeautifulSoup

def gethttptext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillunivlist(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[4].string])

def printunivlist(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        if u[2]==None:
            u[2]='None'
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo=[]
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming-zongbang-2020.html'
    html=gethttptext(url)
    fillunivlist(uinfo,html)
    printunivlist(uinfo,124)

main()
