import re
import requests
import pymysql
import json
import time
def gethttptext(url):
    try:
        header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                  "Cache-Control": "max-age=0",
                  "Connection": "keep-alive",
                  "Host": "maoyan.com",
                  "Referer": "http://maoyan.com/board",
                  "Upgrade-Insecure-Requests": "1",
                  "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36"}
        r=requests.get(url,headers=header,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        #print("请求失败\n")
        return ""
def parsepage(html):
    try:
        pattern=re.compile('<dd>.*?board-index.*?>(\d*)</i>.*?data-src="(.*?)".*?name"><a'+
                           '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'+
                           '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
        item=re.findall(pattern,html)
        print(item)
        for infomation in item:

            dic={
                'index':infomation[0],
                'image-url':infomation[1],
                'title':infomation[2],
                'star':infomation[3].strip()[3:],
                'time':infomation[4].strip()[5:],
                'score':infomation[5]+infomation[6],
            }
            yield dic
            '''
            rank=infomation[0]
            imageurl=infomation[1]
            name=infomation[2]
            star=infomation[3].strip()[3:]
            time=infomation[4].strip()[5:]
            score=infomation[5]+infomation[6]
            list.append([rank,name,star,imageurl,time,score])
            '''
    except:
        #print("解析失败")
        return ""
'''
def write_to_file(item):
    with open('./猫眼电影Top100.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(item,ensure_ascii=False)+'\n\n')
'''
def write_to_mysql(item):
    db=pymysql.connect("localhost","root","root","maoyan",charset='utf8')
    cursor=db.cursor()
    #print(item)
    for i in item:
        movie=i
        sql="insert into movies(rank,name,star,imageurl,time,score) values(%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql,movie)
            db.commit()
            print("success")
        except:
            print("lose")
    cursor.close()
    db.close()

def main():
    start_url="https://maoyan.com/board/4?offset="
    '''
    html_text=gethttptext(url)
    items=parsepage(html_text)
    #print(type(items))
    write_to_mysql(items)
    #for item in items:
        #write_to_mysql(item)
        #write_to_file(item)
    '''
    depth=10
    for i in range(depth):
        url=start_url+str(10*i)
        html=gethttptext(url)
        list_data=[]
        parsepage(list_data,html)
        write_to_mysql(list_data)
        print(list_data)
if __name__=="__main__":
    main()


